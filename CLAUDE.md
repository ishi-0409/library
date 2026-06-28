# Library - Claude向けプロジェクトメモ

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
