resource "aws_cloudwatch_log_group" "test-log-group-for-eks" {
  name              = "/aws/eks/${var.CLUSTER_NAME}/cluster"
  retention_in_days = 1

}
