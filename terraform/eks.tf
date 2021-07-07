resource "aws_eks_cluster" "test-eks-cluster" {
  name     = var.CLUSTER_NAME
  role_arn = aws_iam_role.eks-cluster-role.arn

  vpc_config {
    subnet_ids = aws_subnet.test-subnets-for-eks[*].id
  }

  depends_on = [
    aws_iam_role_policy_attachment.test-eks-cluster-AmazonEKSClusterPolicy,
    aws_iam_role_policy_attachment.test-eks-cluster-AmazonEKSVPCResourceController,
  ]
}

resource "aws_eks_node_group" "test-eks-node-group" {
  cluster_name    = aws_eks_cluster.test-eks-cluster.name
  node_group_name = "test-eks-node-group"
  node_role_arn   = aws_iam_role.eks-cluster-role.arn
  subnet_ids      = aws_subnet.test-subnets-for-eks[*].id

  scaling_config {
    desired_size = 1
    max_size     = 1
    min_size     = 1
  }

  depends_on = [
    aws_iam_role_policy_attachment.test-eks-cluster-AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.test-eks-cluster-AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.test-eks-cluster-AmazonEC2ContainerRegistryReadOnly,
  ]
}
