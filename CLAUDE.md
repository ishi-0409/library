# Library - Claude向けプロジェクトメモ

## サービス概要

抽象的なキーワード（「自由」「孤独」など）から古典名著をレコメンドする個人開発Webサービス。ユーザーがキーワードを入力すると、類語辞典で語を拡張しDBの本データとマッチングして候補を返す。本データはGoogle Books APIから事前取得済み。

**技術スタック**
- Frontend: React / Vite（`frontend/src/`）
- Backend: FastAPI + Mangum（`backend/main.py`, `backend/matching.py`）
- DB: PostgreSQL on Amazon RDS（スキーマは `backend/schema.sql`）
- インフラ: AWS Lambda / API Gateway / S3 / CloudFront
- IaC: Terraform

**主要ファイル**
- `backend/main.py` — `/match` エンドポイント
- `backend/matching.py` — 類語辞典 + DBマッチングロジック
- `backend/fetch_books.py` — Google Books APIで本を取得しDBに登録
- `frontend/src/BookCard.jsx` — 本カードのUIコンポーネント

**機能追加パターン（例: カラム追加時）**
`books`テーブルにカラムを追加する場合は `schema.sql` → `fetch_books.py` → `matching.py` → `main.py` → JSX の順に対応する。

## インフラ構成

```
Internet
├── CloudFront → S3（public）← フロントエンド
└── API Gateway → Lambda（private）→ RDS（private）
```

- VPC: 10.0.0.0/16、プライベートサブネット x2（ap-northeast-1a / 1c）
- S3 Gateway Endpoint（無料）追加済み
- Lambda SG: egress全許可
- RDS SG: Lambda SGからの5432のみ許可
- CloudWatchログなし（VPC Endpoint未追加のため意図的な選択）

## 注意点

- ローカルPCからRDSに直接接続不可（privateのため）
- データ操作が必要な場合はLambda経由で行う必要がある
- RDSは使わないときに停止してコスト削減: `aws rds stop-db-instance --db-instance-identifier library-db`
- 月額コスト: RDS稼働時約$19/月、停止時約$3/月
