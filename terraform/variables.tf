variable "CLUSTER_NAME" {
  default = "test-eks-cluster"
  type    = string
}

variable "REGION" {
  default = "us-east-1"
  type    = string
}

variable "ACCESS_KEY" {
  type = string
}

variable "SECRET_KEY" {
  type    = string
}