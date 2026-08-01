# ユーザーの入力した単語に対してDBに登録されている本それぞれの単語とマッチさせる機能 (DynamoDB対応)

import os
import time
import requests
import boto3
from dotenv import load_dotenv

load_dotenv()

TABLE_NAME = os.getenv("TABLE_NAME", "library-books")
REQUESTS_TABLE_NAME = os.getenv("REQUESTS_TABLE_NAME", "library-requests")
AWS_REGION = os.getenv("AWS_REGION", "ap-northeast-1")
API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

GENRE_COLORS = {
    '哲学':     '#7C3AED',
    '文学':     '#DC2626',
    'ビジネス': '#2563EB',
    '心理学':   '#059669',
    '歴史':     '#D97706',
    '社会学':   '#0891B2',
    '経済学':   '#65A30D',
    '政治':     '#B91C1C',
    '宗教':     '#92400E'
}

# 類語辞典 key=DBにある単語 value=想定されるユーザーの入力
SYNONYMS = {
    "孤独":       ["孤立", "一人ぼっち", "寂しい", "ひとり", "孤独感", "孤立感", "誰もいない", "ひとりぼっち"],
    "疎外感":     ["疎外", "のけ者", "浮いている", "馴染めない", "居場所がない", "除け者"],
    "自己嫌悪":   ["自分が嫌い", "自己否定", "自分を責める", "ダメな自分", "自分が情けない"],
    "人間不信":   ["人が信じられない", "人間不信", "他人が怖い", "人間が嫌い", "誰も信用できない"],
    "死":         ["死亡", "生死", "逝く", "亡くなる", "死にたい", "消えたい", "命を絶つ"],
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
    "正義":       ["公正", "公平", "善悪", "倫理", "道徳"],
    "革命":       ["変革", "改革", "体制打破", "反乱", "抵抗", "蜂起"],
    "全体主義":   ["独裁", "管理社会", "監視社会", "自由のない社会", "支配体制"],
    "戦争":       ["争い", "戦い", "紛争", "暴力", "殺し合い", "武力"],
    "家族":       ["兄弟", "子供", "母親", "父親", "家庭", "親子", "肉親"],
    "人生の意味": ["生きる意味", "なぜ生きるのか", "生きがい", "目的", "意義", "なんのために"],
    "信仰":       ["宗教", "信じる", "神様", "祈り", "救い", "神への信仰"],
    "記憶":       ["思い出", "過去", "忘れない", "忘れられない", "懐かしい", "回想"],
    "時間":       ["時の流れ", "老い", "年をとる", "過去", "未来", "永遠"],
    "社会批判":   ["社会への不満", "世の中への怒り", "社会の矛盾", "不公平な社会"],
    "幸福":       ["幸せ", "しあわせ", "喜び", "充実", "満足", "豊か"],
    "平等":       ["差別", "不平等", "格差", "公平", "同じ権利"],
    "自己破壊":   ["自滅", "自分を傷つける", "破滅", "自己崩壊", "墜落"],
    "挫折":       ["失敗", "うまくいかない", "夢が叶わない", "敗北", "くじける"],
    "官僚制":           ["お役所仕事", "縦割り行政", "マニュアル社会", "トップダウン組織"],
    "合理的支配":       ["法律主義", "ルール社会", "実力主義組織", "公的な権限"],
    "ハビトゥス":       ["育ちの良さ", "無意識の習慣", "身に染みついた癖", "階層による好み"],
    "文化資本":         ["家庭の教養", "親の学歴の影響", "実家の読書習慣", "隠れた格差"],
    "社会的連帯":       ["地域のつながり", "コミュニティの絆", "相互扶助", "社会の結束"],
    "アノミー":         ["無連帯", "価値観の崩壊", "社会的孤立", "道徳の空白"],
    "物象化":           ["人間関係の損得勘定", "拝金主義", "人間疎外", "効率第一主義"],
    "疎外":             ["組織の歯車", "やりがいの搾取", "社会的な孤立感", "労働の虚しさ"],
    "ヘゲモニー":       ["世間の空気", "主導権争い", "文化的な支配", "常識の押し付け"],
    "規律権力":         ["同調圧力", "校則縛り", "自己管理社会", "見えない監視"],
    "生政治":           ["国家の人口管理", "健康強制社会", "感染症規制", "国民のデータ化"],
    "ナショナリズム":   ["愛国心", "自国第一主義", "民族意識", "地元愛"],
    "グローバリゼーション": ["世界の一体化", "国際化", "世界標準", "ボーダレス社会"],
    "消費主義":         ["大量消費", "買い物依存", "ブランド", "物質主義"],
    "リスク社会":       ["現代の不条理", "想定外の災害", "科学技術の副作用", "予測不能な未来"],
    "ジェンダー":       ["男らしさ女らしさ", "男女格差", "男女", "性別"],
}

# ユーザーの入力に対して類語辞典のkeyをプラスする
def expand_input(user_input: str) -> str:
    expanded = user_input
    for canonical, synonyms in SYNONYMS.items():
        for synonym in synonyms:
            if synonym in user_input and canonical not in expanded:
                expanded += " " + canonical
    return expanded

def get_dynamodb_table():
    dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
    return dynamodb.Table(TABLE_NAME)

def get_requests_table():
    dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
    return dynamodb.Table(REQUESTS_TABLE_NAME)

# データベースにある本とマッチングさせる機能 (DynamoDB)
def match_books(user_input: str):
    expanded = expand_input(user_input)
    table = get_dynamodb_table()

    response = table.scan()
    items = response.get("Items", [])

    while "LastEvaluatedKey" in response:
        response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
        items.extend(response.get("Items", []))

    expanded_lower = expanded.lower()

    results = []
    for item in items:
        keywords = item.get("ideology_keywords", [])
        score = 0
        for kw in keywords:
            if kw.lower() in expanded_lower:
                score += 1

        genre_name = item.get("genre_name", "")
        genre_color = item.get("color_code") or GENRE_COLORS.get(genre_name, '#7C3AED')

        results.append((
            item.get("title", ""),
            item.get("author", ""),
            keywords,
            item.get("cover_image_url", ""),
            item.get("author_message", ""),
            genre_name,
            genre_color,
            score,
            item.get("preview_url", ""),
        ))

    results.sort(key=lambda x: x[7], reverse=True)
    return results

# 本のリクエストを保存する機能
def add_book_request(title: str, author: str, genre: str, reason_keywords: str):
    table = get_requests_table()
    req_id = f"req_{int(time.time() * 1000)}"
    item = {
        "id": req_id,
        "title": title,
        "author": author,
        "genre": genre,
        "reason_keywords": reason_keywords,
        "status": "pending",
        "created_at": int(time.time())
    }
    table.put_item(Item=item)
    return item

# 届いているリクエスト一覧を取得する機能 (管理者用)
def get_pending_requests():
    table = get_requests_table()
    response = table.scan()
    items = response.get("Items", [])
    items.sort(key=lambda x: x.get("created_at", 0), reverse=True)
    return items

if __name__ == "__main__":
    test_inputs = [
        "孤独や虚無感を感じている",
        "一人ぼっちで寂しい",
    ]
    for text in test_inputs:
        expanded = expand_input(text)
        print(f"入力: {text} -> 展開: {expanded}")
