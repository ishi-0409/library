# Google Books APIから情報を自動取得し、DynamoDBに新しい本を登録するツール

import os
import sys
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

def fetch_and_add_book(title: str, author: str, genre: str, keywords: list):
    """Google Books APIから情報を取得してDynamoDBに保存する"""
    print(f"\n📖 Google Books APIから情報検索中: 『{title}』 ({author})...")

    url = "https://www.googleapis.com/books/v1/volumes"
    query = f"intitle:{title} inauthor:{author}"
    params = {"q": query, "maxResults": 1}
    if API_KEY:
        params["key"] = API_KEY

    try:
        res = requests.get(url, params=params, timeout=5).json()
        items = res.get("items", [])
    except Exception as e:
        print(f"❌ API接続エラー: {e}")
        items = []

    if items:
        info = items[0].get("volumeInfo", {})
        desc = info.get("description", "")
        author_msg = desc[:100] + "..." if desc else f"『{title}』の古典名著。"
        cover_url = info.get("imageLinks", {}).get("thumbnail", "")
        preview_url = info.get("previewLink", "")
        
        # ISBNの取得
        isbn = title
        for identifier in info.get("industryIdentifiers", []):
            if identifier.get("type") == "ISBN_13":
                isbn = identifier.get("identifier")
                break
        
        book_title = info.get("title", title)
        book_author = ", ".join(info.get("authors", [author]))
    else:
        print("⚠️ APIで本が見つからなかったため、基本情報で作成します。")
        cover_url = ""
        preview_url = ""
        author_msg = f"『{title}』の古典名著。"
        isbn = title
        book_title = title
        book_author = author

    # DynamoDBに投入するデータ構造
    item = {
        "id": f"isbn_{isbn}",
        "title": book_title,
        "author": book_author,
        "genre_name": genre,
        "color_code": GENRE_COLORS.get(genre, "#7C3AED"),
        "ideology_keywords": keywords,
        "author_message": author_msg,
        "cover_image_url": cover_url,
        "preview_url": preview_url
    }

    # DynamoDBへ保存
    dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item=item)

    print(f"✨ DynamoDB登録完了!")
    print(f"  - タイトル: {item['title']}")
    print(f"  - 著者: {item['author']}")
    print(f"  - ジャンル: {item['genre_name']} ({item['color_code']})")
    print(f"  - キーワード: {', '.join(item['ideology_keywords'])}\n")

def interactive_mode():
    """対話形式で本を追加する"""
    print("=" * 50)
    print(" 📚 DynamoDB 新規本追加ツール (Google Books API連携)")
    print("=" * 50)

    title = input("本のタイトルを入力してください: ").strip()
    if not title:
        print("タイトルは必須です。")
        return

    author = input("著者名を入力してください: ").strip()
    
    print("\n選択可能なジャンル:")
    for g in GENRE_COLORS.keys():
        print(f" - {g}")
    genre = input("ジャンル名を入力してください (例: 哲学): ").strip() or "哲学"

    kw_input = input("マッチングキーワードをカンマ区切りで入力してください (例: 自由, 孤独, 成長): ").strip()
    keywords = [k.strip() for k in kw_input.split(",") if k.strip()]

    fetch_and_add_book(title, author, genre, keywords)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Google Books APIから本情報を取得してDynamoDBに登録する")
    parser.add_argument("--title", help="本のタイトル")
    parser.add_argument("--author", default="", help="著者名")
    parser.add_argument("--genre", default="哲学", help="ジャンル名")
    parser.add_argument("--keywords", help="カンマ区切りのキーワード (例: 自由,孤独)")

    args = parser.parse_args()

    if args.title:
        kw_list = [k.strip() for k in args.keywords.split(",") if k.strip()] if args.keywords else []
        fetch_and_add_book(args.title, args.author, args.genre, kw_list)
    else:
        interactive_mode()
