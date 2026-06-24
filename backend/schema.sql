
# 本のジャンル
CREATE TABLE genres (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(50)  NOT NULL UNIQUE,  -- ジャンル名（例: 哲学, 文学, ビジネス）
    color_code  VARCHAR(7)   NOT NULL,          -- フロントで色分けするためのカラーコード（例: #4A90E2）
    created_at  TIMESTAMP    DEFAULT NOW()
);

# 本のデータ
CREATE TABLE books (
    id                  SERIAL PRIMARY KEY,
    title               VARCHAR(255) NOT NULL,
    author              VARCHAR(255) NOT NULL,
    genre_id            INTEGER      REFERENCES genres(id),   -- genresテーブルへの外部キー
    ideology_keywords   TEXT[]       NOT NULL DEFAULT '{}',   -- マッチングに使うキーワードの配列
    author_message      TEXT,                                 -- 著者の一言（本の紹介文から抽出）
    cover_image_url     TEXT,                                 -- Google Books APIから取得した表紙画像のURL
    preview_url         TEXT,                                 -- Google Books 試し読みリンク
    isbn                VARCHAR(20)  UNIQUE,                  -- 同じ本が重複登録されないようにISBNをユニークにする
    created_at          TIMESTAMP    DEFAULT NOW()
);

CREATE INDEX idx_books_ideology_keywords ON books USING GIN (ideology_keywords);

CREATE INDEX idx_books_genre_id          ON books (genre_id);

# ジャンル別カラー
INSERT INTO genres (name, color_code) VALUES
    ('哲学',     '#7C3AED'),
    ('文学',     '#DC2626'),
    ('ビジネス', '#2563EB'),
    ('心理学',   '#059669'),
    ('歴史',     '#D97706'),
    ('社会学',   '#0891B2'),
    ('経済学',   '#65A30D'),
    ('政治',     '#B91C1C'),
    ('宗教',     '#92400E');
