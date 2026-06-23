# 追加機能実装プラン

## Context

`test.md` の「追加機能(検討)」セクションに記載されている6項目のうち、現在のサービスに最も価値をもたらす機能を優先順位付けして実装する。現状の `/match` エンドポイントは「思想キーワードによる全文マッチ」のみで、ジャンル絞り込み（マスト機能として定義されているが未実装）や否定検索などが欠けている。

---

## 実装する機能（優先順）

### 1. ジャンル絞り込み機能（マスト機能・未実装）

**背景:** `test.md` のマスト機能に「ジャンルを選択できる機能」が明記されているが現在未実装。

**Backend — `backend/main.py`**
- `/match` エンドポイントに `genre: str = None` クエリパラメータを追加
- `match_books(user_input, genre=None)` にシグネチャ変更

**Backend — `backend/matching.py`**
- `match_books` に `genre` 引数を追加
- SQL に `WHERE g.name = %s` 条件を動的に付与（None のときは全ジャンル対象）
- `/genres` エンドポイントを `main.py` に追加して全ジャンル一覧を返す

**Frontend — `frontend/src/App.jsx`**
- `genre` state を追加
- 検索時に `genre` パラメータを fetch URL に付与

**Frontend — 新ファイル `frontend/src/GenreFilter.jsx`**
- ジャンル一覧を API から取得して色付きチップとして表示
- 選択中のジャンルをハイライト、「全て」ボタンで解除

---

### 2. 作品名・著者名検索

**背景:** `test.md` 追加機能1番目。ユーザーが具体的な本や著者を探せるようにする。

**Backend — `backend/main.py`**
- `/search?q=キーワード` エンドポイントを新規追加
- books テーブルの `title` と `author` に対して `ILIKE %キーワード%` で全文検索

**Frontend — `frontend/src/SearchForm.jsx`**
- 検索モードトグル（「思想で探す」/ 「タイトル・著者で探す」）を追加
- モードに応じて `handleSearch` が呼ぶ API を切り替える（`App.jsx` 経由）

---

### 3. 否定表現対応

**背景:** `test.md` 追加機能2番目。「自由でない」と入力したときに「自由」キーワードの本がヒットしてしまう問題の解消。

**Backend — `backend/matching.py`**
- `extract_negations(user_input)` 関数を新規追加
  - パターン: `〜ではない`, `〜でない`, `〜じゃない`, `〜ない`, `〜なく`
  - 類義語展開前のキーワードを抽出して除外リストを構築
- `match_books` の SQL を拡張:
  ```sql
  AND NOT (b.ideology_keywords && %s::text[])  -- 除外キーワード配列
  ```
- API レスポンスに `excluded_keywords` フィールドを追加

**Frontend — `frontend/src/App.jsx`**
- 除外キーワードがある場合に「除外: 〜」バッジを検索バーの下に表示

---

### 4. 本の登録要望機能

**背景:** `test.md` 追加機能5番目。ユーザーエンゲージメント向上。

**Database — `backend/schema.sql` に追記**
```sql
CREATE TABLE book_requests (
    id          SERIAL PRIMARY KEY,
    title       VARCHAR(255) NOT NULL,
    author      VARCHAR(255),
    reason      TEXT,
    created_at  TIMESTAMP DEFAULT NOW()
);
```

**Backend — `backend/main.py`**
- `POST /request` エンドポイントを追加（Pydantic モデルで受け取り）

**Frontend — 新ファイル `frontend/src/RequestModal.jsx`**
- 「本を追加リクエスト」ボタンをページ下部に常時表示
- モーダル内にタイトル・著者・理由のフォーム

---

### 5. 大学図書館リンク（シンプル実装）

**背景:** `test.md` 追加機能4番目。外部 API 連携は複雑なため、ISBN からカーリルへのリンクを生成するだけの軽量実装にする。

**Backend — `backend/main.py`**
- `/match` レスポンスに `isbn` フィールドを追加（現在未返却）

**Frontend — `frontend/src/BookCard.jsx`**
- isbn が存在する場合に「図書館で探す」リンクを追加
- URL: `https://calil.jp/book/{isbn}` (カーリル公共図書館 API)

---

## 実装しない機能

- **Google Books API プレビュー**: `preview_link` が DB に保存されていないため、スキーマ変更とデータ再取得が必要。コスト対効果が低い。
- **著者で絞ってワード検索**: 機能2（作品名・著者名検索）と機能1（ジャンル絞り込み）の組み合わせで代替可能。

---

## 変更ファイル一覧

| ファイル | 変更種別 |
|---|---|
| `backend/main.py` | 変更: `/match` にジャンルパラム追加、`/genres`・`/search`・`POST /request` エンドポイント追加 |
| `backend/matching.py` | 変更: ジャンル絞り込み・否定表現抽出ロジック追加 |
| `backend/schema.sql` | 変更: `book_requests` テーブル追加 |
| `frontend/src/App.jsx` | 変更: genre state、除外キーワード表示、モード切り替え対応 |
| `frontend/src/SearchForm.jsx` | 変更: 検索モードトグル追加 |
| `frontend/src/BookCard.jsx` | 変更: isbn フィールドを受け取り図書館リンク表示 |
| `frontend/src/GenreFilter.jsx` | 新規: ジャンル絞り込みチップコンポーネント |
| `frontend/src/RequestModal.jsx` | 新規: 本の登録要望モーダルコンポーネント |

---

## 検証方法

1. **ジャンル絞り込み**: 「哲学」を選択した状態で思想検索し、全結果のジャンルが「哲学」のみであることを確認
2. **タイトル・著者検索**: 「カフカ」で著者検索し、カフカ作品のみが返ることを確認
3. **否定表現**: 「自由ではない」で検索し、ideology_keywords に「自由」を含む本が結果に出ないことを確認
4. **要望機能**: フォームからリクエストを送信し、PostgreSQL の `book_requests` テーブルに行が追加されることを確認
5. **図書館リンク**: ISBN がある本のカードで「図書館で探す」リンクをクリックし、カーリルの該当ページが開くことを確認
