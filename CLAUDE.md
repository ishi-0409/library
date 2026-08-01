# Library - Claude向けプロジェクトメモ

## サービス概要

抽象的なキーワード（「自由」「孤独」など）から古典名著をレコメンドする個人開発Webサービス。ユーザーがキーワードを入力すると、類語辞典で語を拡張しDBの本データとマッチングして候補を返す。



**技術スタック**
- Frontend: React / Vite（`frontend/src/`）
- Backend: FastAPI + Mangum（`backend/main.py`, `backend/matching.py`）
- DB: Amazon DynamoDB (`library-books`, `library-requests`)
- インフラ: AWS Lambda / API Gateway / S3 / CloudFront（完全サーバーレス構成）
- IaC: Terraform
- CI/CD: GitHub Actions（`git push` で自動テスト・ビルド・AWSデプロイ）

## ディレクトリ構造と主要ファイル

```text
library/
├── .github/
│   └── workflows/
│       └── deploy.yml     # GitHub Actions 自動デプロイパイプライン定義
├── backend/
│   ├── main.py            # FastAPI アプリ本体（/match, /requests エンドポイント）
│   ├── matching.py        # 類語辞書 ＋ DynamoDB (boto3) ロジック
│   ├── import_books_csv.py# CSVファイルからの本大量一括登録ツール
│   ├── sample_books.csv   # 一括インポート用サンプルCSVファイル
│   └── package/           # AWS Lambda デプロイ用モジュールパッケージ群
├── frontend/
│   ├── src/
│   │   ├── App.jsx        # メインコンポーネント（検索API呼び出し・リクエスト表示）
│   │   ├── BookCard.jsx   # 本カード表示コンポーネント
│   │   └── BookRequestModal.jsx # ユーザー本追加リクエストモーダル
├── terraform/
│   ├── main.tf            # Provider, S3, CloudFront 定義
│   ├── lambda.tf          # Lambda 関数, API Gateway, IAM ロール/ポリシー定義
│   ├── dynamodb.tf        # DynamoDB テーブル (library-books, library-requests) 定義
│   ├── outputs.tf         # CloudFront URL, API Gateway URL, DynamoDBテーブル名
│   └── variables.tf       # 共通変数定義
└── CLAUDE.md              # 本ドキュメント
```

## インフラ構成図

```
Internet
├── CloudFront → S3（public）← フロントエンド (React)
└── API Gateway → Lambda → DynamoDB (`library-books`, `library-requests`)
```

- **完全サーバーレス構成**: VPCなし、アクセスの無い時間は基本料 **$0/月**。
- **CI/CD 自動デプロイ**: GitHub に `git push main` すると、GitHub Actions が自動デプロイ。

