resource "aws_vpc" "test-vpc-for-eks" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "main"
  }
}

resource "aws_subnet" "test-subnets-for-eks" {
  count = 2

  availability_zone = data.aws_availability_zones.available.names[count.index]
  cidr_block        = cidrsubnet(aws_vpc.test-vpc-for-eks.cidr_block, 8, count.index)
  vpc_id            = aws_vpc.test-vpc-for-eks.id

  tags = {
    "kubernetes.io/cluster/${aws_eks_cluster.test-eks-cluster.name}" = "shared"
  }
}
