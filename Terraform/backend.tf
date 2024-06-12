terraform {
  backend "s3" {
    bucket = "jassoft-terraform-states"
    key    = "ec2-lambda"
    region = "eu-west-2"
  }
}