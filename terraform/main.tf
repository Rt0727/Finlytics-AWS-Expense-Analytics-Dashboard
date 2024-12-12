provider "aws" {
  region = "us-west-2"
}

resource "aws_ec2_instance" "web_server" {
  ami             = var.ec2_ami
  instance_type   = var.instance_type
  key_name        = var.key_name
  subnet_id       = var.subnet_id
  security_group  = var.security_group
  associate_public_ip_address = true
}

resource "aws_rds_instance" "expense_db" {
  engine           = "postgres"
  instance_class   = "db.t3.micro"
  allocated_storage = 20
  db_name          = var.db_name
  username         = var.db_username
  password         = var.db_password
  instance_identifier = "expense-db"
  publicly_accessible = true
}

resource "aws_s3_bucket" "data_bucket" {
  bucket = "expense-dashboard-data-bucket"
}

resource "aws_iam_role" "s3_access_role" {
  name = "s3-access-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_policy" "s3_access_policy" {
  name        = "s3-access-policy"
  description = "Allow EC2 to access the S3 bucket"
  policy      = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action   = "s3:GetObject",
      Effect   = "Allow",
      Resource = "${aws_s3_bucket.data_bucket.arn}/*"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "role_policy_attachment" {
  role       = aws_iam_role.s3_access_role.name
  policy_arn = aws_iam_policy.s3_access_policy.arn
}