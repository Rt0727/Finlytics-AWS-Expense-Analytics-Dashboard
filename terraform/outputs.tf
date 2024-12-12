output "ec2_public_ip" {
  value = aws_ec2_instance.web_server.public_ip
}

output "rds_endpoint" {
  value = aws_rds_instance.expense_db.endpoint
}

output "s3_bucket_url" {
  value = aws_s3_bucket.data_bucket.website_endpoint
}