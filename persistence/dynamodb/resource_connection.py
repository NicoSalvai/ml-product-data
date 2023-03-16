import boto3


def resource():
    return boto3.resource('dynamodb',
                          aws_access_key_id="local",
                          aws_secret_access_key="local",
                          region_name="us-west-2",
                          endpoint_url="http://localhost:8000")


def get_table(table_name):
    return resource().Table(table_name)
