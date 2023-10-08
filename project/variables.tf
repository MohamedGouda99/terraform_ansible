variable "access_key" {
  type        = string
  description = "AWS access key"
  
}

variable "secret_key" {
  type        = string
  description = "AWS secret key"
  
}

variable "aws_region" {
  type    = string
  default = "us-east-2"
}

variable "vpc_cidr_block" {}

variable "subnet_cidr_block" {}

variable "avail_zone" {}

variable "env_prefix" {}

variable "my_ip" {}

variable "instance_type" {}


variable public_cidr_blocks{}

variable "private_cidr_blocks" {}
