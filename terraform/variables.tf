variable "aws_region" {
  default = "ap-northeast-1"
}

variable "project_name" {
  default = "library"
}

variable "db_name" {
  default = "librarydb"
}

variable "db_username" {
  default = "postgres"
}

variable "db_password" {
  description = "RDSのパスワード"
  sensitive   = true
}

variable "my_ip" {
  description = "自分のIPアドレス"
}

