variable "aws_region" {
  description = "Value of the AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "public_ssh_file" {
  type    = string
  default = "~/.ssh/id_rsa.pub"
}

variable "cluster_name" {
  type    = string
  default = "eks-cluster"
}

variable "vpc_id" {
  type    = string
  default = "vpc-0df2a9cb464f310b1"
}

variable "subnet_ids" {
  type = list(string)
  default = [
    "subnet-00f2b4efa959df645", "subnet-0163b44e535cdf199", "subnet-0c529cd39835b19b2", "subnet-07590163ae209b5f4", "subnet-08876ac86ca7b082b"
  ]
}

variable "instance_type" {
  type    = list(string)
  default = ["t3.medium"]
}

variable "aws_auth_accounts" {
  type    = list(string)
  default = ["095915172525"]
}

