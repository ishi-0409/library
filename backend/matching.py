# ユーザーの入力した単語に対してDBに登録されている本それぞれの単語とマッチさせる機能

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
HOST     = os.getenv("POSTGRES_HOST")
USER     = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME  = os.getenv("POSTGRES_DB")

# 類語辞典 key=DBにある単語 value=想定されるユーザーの入力
SYNONYMS = {
    "孤独":       ["孤立", "一人ぼっち", "寂しい", "ひとり", "孤独感", "孤立感", "誰もいない", "ひとりぼっち"],
    "疎外感":     ["疎外", "のけ者", "浮いている", "馴染めない", "居場所がない", "除け者"],
    "自己嫌悪":   ["自分が嫌い", "自己否定", "自分を責める", "ダメな自分", "自分が情けない"],
    "人間不信":   ["人が信じられない", "人間不信", "他人が怖い", "人間が嫌い", "誰も信用できない"],
    "死":         ["死亡", "命", "生死", "逝く", "亡くなる", "終わり", "死にたい", "消えたい"],
    "不安":       ["怖い", "恐怖", "おびえる", "心配", "びくびく", "ドキドキ", "焦り", "恐れ"],
    "絶望":       ["希望がない", "もう終わり", "諦め", "先が見えない", "どうにもならない"],
    "虚無主義":   ["虚無感", "虚しい", "空虚", "意味がない", "むなしい", "虚無", "ニヒリズム"],
    "不条理":     ["理不尽", "納得できない", "意味がわからない", "理由がない", "理不尽さ"],
    "愛":         ["恋愛", "愛情", "恋", "好き", "片思い", "両思い", "恋心", "愛する"],
    "失恋":       ["失恋", "振られた", "別れ", "フラれた", "恋が終わった", "片思い終わり"],
    "自由":       ["解放", "束縛", "縛られている", "自立", "自分らしく", "型にはまらない"],
    "苦しみ":     ["苦しい", "つらい", "辛さ", "痛み", "悲しい", "悲しみ", "しんどい", "きつい"],
    "喪失":       ["失う", "なくす", "失った", "消えた", "失われた", "奪われた"],
    "成長":       ["大人になる", "成熟", "変わる", "自己発見", "気づき", "自分探し"],
    "青春":       ["若い頃", "学生時代", "思春期", "若さ", "10代", "高校生", "大学生"],
    "狂気":       ["狂う", "正気でない", "正気を失う", "おかしくなる", "精神的に追い詰められる"],
    "権力":       ["支配", "権威", "強者", "支配者", "コントロール", "操る"],
    "正義":       ["公正", "公平", "善悪", "善", "悪", "倫理", "道徳"],
    "革命":       ["変革", "改革", "体制打破", "反乱", "抵抗", "蜂起"],
    "全体主義":   ["独裁", "管理社会", "監視社会", "自由のない社会", "支配体制"],
    "戦争":       ["争い", "戦い", "紛争", "暴力", "殺し合い", "武力"],
    "家族":       ["親", "兄弟", "子供", "母", "父", "家庭", "親子"],
    "人生の意味": ["生きる意味", "なぜ生きるのか", "生きがい", "目的", "意義", "なんのために"],
    "信仰":       ["神", "宗教", "信じる", "神様", "祈り", "救い"],
    "記憶":       ["思い出", "過去", "忘れない", "忘れられない", "懐かしい", "回想"],
    "時間":       ["時の流れ", "老い", "年をとる", "過去", "未来", "永遠"],
    "社会批判":   ["社会への不満", "世の中への怒り", "社会の矛盾", "不公平な社会"],
    "幸福":       ["幸せ", "しあわせ", "喜び", "充実", "満足", "豊か"],
    "平等":       ["差別", "不平等", "格差", "公平", "同じ権利"],
    "自己破壊":   ["自滅", "自分を傷つける", "破滅", "自己崩壊", "墜落"],
    "挫折":       ["失敗", "うまくいかない", "夢が叶わない", "敗北", "くじける"],
}

# ユーザーの入力に対して類語辞典のkeyをプラスする
def expand_input(user_input: str) -> str:
    expanded = user_input
    
    for canonical, synonyms in SYNONYMS.items():
        for synonym in synonyms:
            if synonym in user_input and canonical not in expanded:
                expanded += " " + canonical
    return expanded

# データベースにある本とマッチングさせる機能
def match_books(user_input: str):
    
    expanded = expand_input(user_input)
    if DATABASE_URL:
        conn = psycopg2.connect(DATABASE_URL)
    else:
        conn = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DB_NAME)
    cur = conn.cursor()

    # DBにある本の単語を一行ずつ展開
    # booksテーブルのidに対してgenreテーブルのidを結合

    cur.execute("""
        SELECT b.title, b.author, b.ideology_keywords,
          b.cover_image_url, b.author_message,
          g.name as genre_name, g.color_code,
          (SELECT COUNT(*) FROM unnest(b.ideology_keywords) k
           WHERE %s ILIKE '%%' || k || '%%') as score
        FROM books b
        LEFT JOIN genres g ON b.genre_id = g.id
        ORDER BY score DESC
    """, (expanded,))

    results = cur.fetchall()
    cur.close()
    conn.close()
    return results



if __name__ == "__main__":
    test_inputs = [
        "孤独や虚無感を感じている",
        "一人ぼっちで寂しい",        
        "生きる意味がわからない",     
        "理不尽な世界が嫌だ",        
    ]
    for text in test_inputs:
        expanded = expand_input(text)
        print(f"入力: {text}")
        print(f"展開: {expanded}")
        print()
