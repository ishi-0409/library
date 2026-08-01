resource "aws_dynamodb_table" "books" {
  name         = "${var.project_name}-books"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }

  tags = {
    Name = "${var.project_name}-books"
  }
}

resource "aws_dynamodb_table" "requests" {
  name         = "${var.project_name}-requests"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }

  tags = {
    Name = "${var.project_name}-requests"
  }
}
