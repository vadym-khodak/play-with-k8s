output "endpoint" {
  value = aws_eks_cluster.test-eks-cluster.endpoint
}

output "kubeconfig-certificate-authority-data" {
  value = aws_eks_cluster.test-eks-cluster.certificate_authority[0].data
}
