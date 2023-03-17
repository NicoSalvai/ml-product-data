from persistence.dynamodb.resource_connection import get_table
from boto3.dynamodb.conditions import Attr

def get_searches_table():
    return get_table('searches')


def get_searches(enabled=True, table=None):
    table = table if table is not None else get_searches_table()
    result = table.scan(FilterExpression=Attr('enabled').eq(enabled))
    return result['Items']

def update_search_enabled(id: str, enabled:bool, table=None):
    table = table if table is not None else get_searches_table()
    result = table.update_item(
        Key={
            'id': id
        },
        UpdateExpression='SET enabled = :val1',
        ExpressionAttributeValues={
            ':val1': enabled
        }
    )
    print(result)