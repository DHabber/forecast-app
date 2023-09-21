
provider "aws" {
  region = var.aws_region
}

module "eks" {
  #checkov:skip=CKV_TF_1:"echo pass"
  source  = "terraform-aws-modules/eks/aws"
  # source = "terraform-aws-modules/terraform-aws-eks.git?ref=d4e6c15"
  # source = "github.com/terraform-aws-modules/terraform-aws-acm?ref=21d41965c40fbbb10710ab36404023e4379c7524"
  version = "19.16.0"

  cluster_name    = var.cluster_name
  cluster_version = "1.27"

  cluster_endpoint_public_access = true

  cluster_addons = {
    coredns = {
      most_recent = true
    }
    kube-proxy = {
      most_recent = true
    }
    vpc-cni = {
      most_recent = true
    }
  }

  vpc_id                   = var.vpc_id
  subnet_ids               = var.subnet_ids
  control_plane_subnet_ids = var.subnet_ids

  eks_managed_node_groups = {
    group01 = {
      min_size     = 2
      max_size     = 2
      desired_size = 2
      disk_size    = 8

      instance_types = var.instance_type
      capacity_type  = "SPOT"
      block_device_mappings = {
        xvda = {
          device_name = "/dev/xvda"
          ebs = {
            volume_size           = 8
            volume_type           = "gp3"
            encrypted             = true
            delete_on_termination = true
          }
        }
      }
    }
  }

  aws_auth_accounts = var.aws_auth_accounts

  tags = {
    Cluster = "k8s"
    Environment = "dev"
    Terraform   = "true"
    Name        = "EKS_node"
  }
}

