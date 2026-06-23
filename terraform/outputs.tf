output "cloudfront_url" {
  description = "フロントエンドのURL"
  value       = "https://${aws_cloudfront_distribution.frontend.domain_name}"
}

output "api_gateway_url" {
  description = "バックエンドAPIのURL"
  value       = aws_apigatewayv2_stage.default.invoke_url
}

output "rds_endpoint" {
  description = "RDSのエンドポイント"
  value       = aws_db_instance.library.address
}

output "s3_bucket_name" {
  description = "フロントエンド用S3バケット名"
  value       = aws_s3_bucket.frontend.id
}
