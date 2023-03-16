import boto3
import os 

def resource():
    return boto3.resource('dynamodb',
                          aws_access_key_id=os.environ["aws_access_key_id"],
                          aws_secret_access_key=os.environ["aws_secret_access_key"],
                          region_name=os.environ["region_name"],
                          endpoint_url=os.environ["endpoint_url"])


def get_table(table_name):
    return resource().Table(table_name)
