import boto3
import logging

from http import HTTPStatus

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        search_criteria = event["Name"]
        logger.info(f'Finding EC2 instances with tag Name containing {search_criteria}')
        ec2_client = boto3.client('ec2')

        paginator = ec2_client.get_paginator('describe_instances')

        page_iterator = paginator.paginate()

        for page in page_iterator:
            for instance in page['Reservations'][0]['Instances']:

                instance_name = next((tag['Value'] for tag in instance['Tags'] if tag['Key'] == 'Name'), None)

                if search_criteria in instance_name:

                    if instance['State']['Name'] == 'running':
                        try:
                            logger.info(f'Stopping instance {instance["InstanceId"]} {instance_name}"')
                            ec2_client.stop_instances(InstanceIds=[instance['InstanceId']])
                        except Exception as e:
                            logger.error(f'Failed to stop instance {instance["InstanceId"]}', exc_info=True)

    except Exception as e:
        logger.error(e, exc_info=True)
        raise Exception('Error occurred during execution')

    return {
        "statusCode": HTTPStatus.OK.value
    }
