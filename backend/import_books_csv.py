# CSVファイルから本データを一括取得・DynamoDBへ自動登録するツール

import os
import sys
import csv
import argparse
import requests
import boto3
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
load_dotenv()

TABLE_NAME = os.getenv("TABLE_NAME")
AWS_REGION = os.getenv("AWS_REGION")
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

def fetch_google_book_info(title: str, author: str):
    url = "https://www.googleapis.com/books/v1/volumes"
    query = f"intitle:{title} inauthor:{author}"
    params = {"q": query, "maxResults": 1}
    if API_KEY:
        params["key"] = API_KEY

    try:
        res = requests.get(url, params=params, timeout=5).json()
        items = res.get("items", [])
        if items:
            info = items[0].get("volumeInfo", {})
            desc = info.get("description", "")
            isbn = title
            for identifier in info.get("industryIdentifiers", []):
                if identifier.get("type") == "ISBN_13":
                    isbn = identifier.get("identifier")
                    break

            return {
                "title": info.get("title", title),
                "author": ", ".join(info.get("authors", [author])),
                "cover_image_url": info.get("imageLinks", {}).get("thumbnail", ""),
                "preview_url": info.get("previewLink", ""),
                "author_message": desc[:100] + "..." if desc else f"『{title}』の古典名著。",
                "isbn": isbn
            }
    except Exception as e:
        print(f"  ⚠️ APIエラー ({title}): {e}")

    return {
        "title": title,
        "author": author,
        "cover_image_url": "",
        "preview_url": "",
        "author_message": f"『{title}』の古典名著。",
        "isbn": title
    }

def import_from_csv(csv_filepath: str):
    if not os.path.exists(csv_filepath):
        print(f"❌ ファイルが見つかりません: {csv_filepath}")
        return

    print("=" * 60)
    print(f" 📚 CSVファイルからの本一括登録ツール ({csv_filepath})")
    print("=" * 60)

    dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
    table = dynamodb.Table(TABLE_NAME)

    books_to_insert = []
    with open(csv_filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row.get("タイトル", "").strip()
            author = row.get("著者", "").strip()
            genre = row.get("ジャンル", "哲学").strip()
            raw_keywords = row.get("キーワード", "").strip()

            if not title:
                continue

            # キーワードをカンマで分割
            keywords = [k.strip() for k in raw_keywords.replace("、", ",").split(",") if k.strip()]
            books_to_insert.append((title, author, genre, keywords))

    print(f"全 {len(books_to_insert)} 冊の本を登録処理開始します...\n")

    success_count = 0
    with table.batch_writer() as batch:
        for idx, (title, author, genre, keywords) in enumerate(books_to_insert, 1):
            info = fetch_google_book_info(title, author)
            item = {
                "id": f"isbn_{info['isbn']}",
                "title": info["title"],
                "author": info["author"],
                "genre_name": genre,
                "color_code": GENRE_COLORS.get(genre, "#7C3AED"),
                "ideology_keywords": keywords,
                "author_message": info["author_message"],
                "cover_image_url": info["cover_image_url"],
                "preview_url": info["preview_url"]
            }
            batch.put_item(Item=item)
            success_count += 1
            print(f"[{idx}/{len(books_to_insert)}] ✨ 登録成功: 『{item['title']}』 ({item['author']}) - キーワード: {len(keywords)}個")

    print("\n" + "=" * 60)
    print(f" 🎉 一括登録完了! 合計 {success_count} 冊の本がDynamoDBに保存されました。")
    print("=" * 60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSVファイルから本データを読み込んでDynamoDBに一括登録する")
    parser.add_argument("csv_file", nargs="?", default="backend/sample_books.csv", help="CSVファイルのパス (デフォルト: backend/sample_books.csv)")
    args = parser.parse_args()

    import_from_csv(args.csv_file)
