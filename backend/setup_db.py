# DBとテーブルを作成する機能

import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv


load_dotenv()


HOST = os.getenv("POSTGRES_HOST")
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")

# データベースを作る機能
def create_database():
    
    conn = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname="postgres")
    
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
    if cur.fetchone():
        
        print(f"データベース '{DB_NAME}' はすでに存在します")
    else:
        
        cur.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"データベース '{DB_NAME}' を作成しました")

    cur.close()
    conn.close()

# 別ファイルで定義したDBテーブル情報をもとにテーブルを作成
def create_tables():
    
    conn = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DB_NAME)
    cur = conn.cursor()

    
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema_path, "r", encoding="utf-8") as f:
        sql = f.read()

    
    cur.execute(sql)
    conn.commit()
    print("テーブルを作成しました")

    cur.close()
    conn.close()


if __name__ == "__main__":
    create_database()
    create_tables()
