import boto3

from moto import mock_aws
from unittest import TestCase

from Lambda.src.ec2_lambda.app import lambda_handler


class Test(TestCase):

    @mock_aws
    def test_lambda_handler_stops_instance_with_matching_name(self):
        ec2 = boto3.resource("ec2", region_name="eu-west-2")

        instances = ec2.create_instances(
            ImageId="ami-0b53285ea6c7a08a7",
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [
                        {"Key": "Name", "Value": "Rowden Test"},
                    ],
                }
            ],
        )
        assert ec2.Instance(instances[0].instance_id).state["Name"] == "running"

        lambda_handler({"Name": "Rowden"}, None)

        assert ec2.Instance(instances[0].instance_id).state["Name"] == "stopped"

    @mock_aws
    def test_lambda_handler_does_not_stop_instance_with_unmatching_name(self):
        ec2 = boto3.resource("ec2", region_name="eu-west-2")

        instances = ec2.create_instances(
            ImageId="ami-0b53285ea6c7a08a7",
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [
                        {"Key": "Name", "Value": "Jon Test"},
                    ],
                }
            ],
        )

        assert ec2.Instance(instances[0].instance_id).state["Name"] == "running"

        lambda_handler({"Name": "Rowden"}, None)

        assert ec2.Instance(instances[0].instance_id).state["Name"] == "running"
