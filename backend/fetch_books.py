# books apiから本の情報を入手して、データベースに登録する機能


import requests
import os
import sys
import psycopg2
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

load_dotenv()
API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

HOST     = os.getenv("POSTGRES_HOST")
USER     = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME  = os.getenv("POSTGRES_DB")


CATEGORY_MAP = {
    "Fiction": "文学",
    "Literary Collections": "文学",
    "Philosophy": "哲学",
    "Business": "ビジネス",
    "Psychology": "心理学",
    "History": "歴史",
}


TITLE_BLACKLIST = ["対訳", "名文選", "トキメキ", "大活字"]

def search_book(title: str):
    
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": title, "maxResults": 10, "key": API_KEY}

    response = requests.get(url, params=params)
    data = response.json()

    if not data.get("items"):
        print("本が見つかりませんでした")
        return

    
    item = next(
        (i for i in data["items"]
         if i.get("volumeInfo", {}).get("description")
         and len(i.get("volumeInfo", {}).get("authors", [])) == 1
         and not any(bad in i.get("volumeInfo", {}).get("title", "") for bad in TITLE_BLACKLIST)),
        data["items"][0]
    )
    info = item.get("volumeInfo", {})

    
    book = {
        "title":             info.get("title"),
        "author":            ", ".join(info.get("authors", [])),
        "ideology_keywords": info.get("categories", []),          
        "author_message":    _extract_first_sentence(info.get("description", "")),
        "cover_image_url":   info.get("imageLinks", {}).get("thumbnail"),
        "isbn":              _get_isbn(info),
        "genre_name":        _map_genre(info.get("categories", [])),
    }

    print(f"取得: {book['title']} / {book['author']}")
    save_book(book)

def save_book(book: dict):
    conn = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DB_NAME)
    cur = conn.cursor()

    genre_id = None
    if book["genre_name"]:
        cur.execute("SELECT id FROM genres WHERE name = %s", (book["genre_name"],))
        row = cur.fetchone()
        if row:
            genre_id = row[0]

    
    cur.execute("""
        INSERT INTO books (title, author, genre_id, ideology_keywords, author_message, cover_image_url, isbn)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (isbn) DO NOTHING
    """, (
        book["title"],
        book["author"],
        genre_id,
        book["ideology_keywords"],
        book["author_message"],
        book["cover_image_url"],
        book["isbn"] or None,
    ))

    conn.commit()
    print(f"保存完了: {book['title']}")

    cur.close()
    conn.close()

def _map_genre(categories: list) -> str:
    
    for category in categories:
        if category in CATEGORY_MAP:
            return CATEGORY_MAP[category]
    return ""

def _extract_first_sentence(text: str) -> str:
    
    if not text:
        return ""
    for sep in ["。", ".", "\n"]:
        idx = text.find(sep)
        if idx != -1:
            return text[:idx + 1]
    
    return text[:100]

def _get_isbn(info: dict) -> str:
    
    for identifier in info.get("industryIdentifiers", []):
        if identifier["type"] == "ISBN_13":
            return identifier["identifier"]
    return ""


BOOKS = [
    # 登録済み: 人間失格, 善の研究, 罪と罰, 戦争と平和, アンナ・カレーニナ, イワン・イリイチの死
    # 登録済み: カラマーゾフの兄弟, 白痴, 悪霊, 地下室の手記
    # 登録済み: 桜の園, 三人姉妹, かもめ, 六号室, 外套・鼻, 死せる魂, 父と子, 巨匠とマルガリータ, ロリータ, はつ恋
    # 登録済み: 老人と海, 武器よさらば, 日はまた昇る, グレート・ギャツビー, 夜はやさし, 響きと怒り, 八月の光, 怒りの葡萄, ハツカネズミと人間, 白鯨
    # 登録済み: ペスト, シーシュポスの神話, 存在と無, ボヴァリー夫人, 感情教育, 赤と黒, パルムの僧院, ゴリオ爺さん, 谷間の百合, レ・ミゼラブル
    # 登録済み: 失われた時を求めて, 異邦人, ノートルダム・ド・パリ, 嘔吐
    # 登録済み: 城, 変身, 審判, ファウスト, 若きウェルテルの悩み, シッダールタ, 車輪の下, デミアン, 荒野のおおかみ
    # 登録済み: 魔の山, ベニスに死す, マルテの手記, チェスの話, ツァラトゥストラはこう語った
    # 登録済み: ハムレット, マクベス, 大いなる遺産, 嵐が丘, ジェーン・エア, ドリアン・グレイの肖像
    # 登録済み: 闇の奥, ダロウェイ夫人, 灯台へ, テス, インドへの道, 1984年, 動物農場, すばらしい新世界
    # 登録済み: 百年の孤独, コレラの時代の愛, 砂の本, 伝奇集, ペドロ・パラモ, 石蹴り, 精霊たちの家, アルテミオ・クルスの死
    # 登録済み: こころ, 雪国, 金閣寺, ノルウェイの森, 砂の女, 阿Q正伝, 少年が来る, 82年生まれ・キム・ジヨン
    # 登録済み: ソクラテスの弁明, 国家, パイドン, ニコマコス倫理学, 政治学, 自省録, 人生の短さについて, 自然について他
    # 登録済み: 方法序説, エチカ, 単子論, 統治二論, 人間本性論, パンセ, 社会契約論, 人間不平等起源論
    # 登録済み: 純粋理性批判, 道徳形而上学の基礎づけ, 精神現象学
    # 登録済み: 意志と表象としての世界, 共産党宣言, 資本論, 善悪の彼岸, 死に至る病, 自由論
    # 登録済み: 論理哲学論考, 存在と時間, 全体主義の起原, 監獄の誕生, 正義論, 消費社会の神話と構造
    # 登録済み(経済学): 国富論, ケインズ一般理論, 隷属への道, 資本主義社会主義民主主義
    # 登録済み(社会学): プロテスタンティズムの倫理, 自殺論, 職業としての政治/学問, 孤独な群衆, アメリカのデモクラシー, 一般言語学講義
    # 登録済み(心理学): 夢判断, 自由からの逃走, 愛するということ, 人生の意味の心理学
    # 登録済み(文化人類学): 野生の思考, 菊と刀
    # 登録済み(政治・文明): 君主論, リヴァイアサン, 文明の衝突, 歴史の終わり, 銃・病原菌・鉄, サピエンス全史/ホモ・デウス
    # 登録済み(思想): オリエンタリズム, 啓蒙の弁証法
]

if __name__ == "__main__":
    for title, author in BOOKS:
        search_book(f"intitle:{title} inauthor:{author}")
