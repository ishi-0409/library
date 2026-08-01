# Library - Claude向けプロジェクトメモ

## サービス概要

抽象的なキーワード（「自由」「孤独」など）から古典名著をレコメンドする個人開発Webサービス。ユーザーがキーワードを入力すると、類語辞典で語を拡張しDBの本データとマッチングして候補を返す。

**技術スタック**
- Frontend: React / Vite（`frontend/src/`）
- Backend: FastAPI + Mangum（`backend/main.py`, `backend/matching.py`）
- DB: Amazon DynamoDB（オンデマンドモード / PAY_PER_REQUEST）
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
│   ├── main.py            # FastAPI アプリ本体（/match エンドポイント・Mangumハンドラー）
│   ├── matching.py        # 類語辞書 ＋ DynamoDB (boto3) スキャン＆マッチ度スコア計算ロジック
│   ├── add_new_book.py    # Google Books API 連携 ＋ DynamoDB 新規本自動登録ツール
│   └── package/           # AWS Lambda デプロイ用モジュールパッケージ群
├── frontend/
│   ├── src/
│   │   ├── App.jsx        # メインコンポーネント（検索API呼び出し・状態管理）
│   │   └── BookCard.jsx   # 本カード表示コンポーネント（ジャンルバッジ・マッチ度・試し読み）
├── terraform/
│   ├── main.tf            # Provider, S3, CloudFront 定義
│   ├── lambda.tf          # Lambda 関数, API Gateway, IAM ロール/ポリシー定義
│   ├── dynamodb.tf        # DynamoDB テーブル (library-books) 定義
│   ├── outputs.tf         # CloudFront URL, API Gateway URL, DynamoDBテーブル名
│   └── variables.tf       # 共通変数定義
└── CLAUDE.md              # 本ドキュメント
```

## インフラ構成図

```
Internet
├── CloudFront → S3（public）← フロントエンド (React)
└── API Gateway → Lambda（VPCなし・超高速起動）→ DynamoDB (`library-books`)
```

- **完全サーバーレス構成**: VPCを撤去したため、LambdaのVPC接続待ちが無く、API応答速度が最速化（数百ミリ秒）。
- **月額コスト**: **$0/月**（AWS無料利用枠・オンデマンドリクエスト従量制のためアクセスの無い時間は基本料 $0）。
- **CI/CD 自動デプロイ**: GitHub に `git push main` すると、GitHub Actions が立ち上がり自動でフロントエンドのビルド、Terraformの適用、CloudFrontキャッシュ削除を実施。

## 運用・本の追加方法

新しい本を追加・登録したい場合は、ローカル環境から統合ツール `add_new_book.py` を実行します。

### 1. 対話形式での登録（推奨）
```bash
python backend/add_new_book.py
```
画面の案内に従って「タイトル」「著者名」「ジャンル」「キーワード」を入力するだけで、Google Books APIから表紙画像・紹介文・試し読みURLを自動取得し、DynamoDB（`library-books`）に一発で保存されます。

### 2. コマンドライン引数での登録
```bash
python backend/add_new_book.py --title "方法序説" --author "デカルト" --genre "哲学" --keywords "合理性,疑念,真理,自己"
```

## 今後の拡張性メモ

- **AI連携 (OpenAI / AWS Bedrock等)**:
  LambdaがVPCの外で直接起動するため、NAT Gatewayなどの高額な固定費なし（$0）で、OpenAI APIやAWS Bedrockへの高速リクエストが可能です。
