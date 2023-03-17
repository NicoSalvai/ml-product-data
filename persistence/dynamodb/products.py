from persistence.dynamodb.resource_connection import get_table


def get_products_table():
    return get_table('products')


def add_product(item, table=None):
    table = table if table is not None else get_products_table()
    result = table.put_item(Item=item)
    print(result)


def update_product_prices(id: str, prices, table=None):
    table = table if table is not None else get_products_table()
    result = table.update_item(
        Key={
            'id': id
        },
        UpdateExpression='SET prices = :val1',
        ExpressionAttributeValues={
            ':val1': prices
        }
    )
    print(result)


def get_product(id, table=None):
    table = table if table is not None else get_products_table()
    result = table.get_item(Key={
        'id': id
    })
    return result

def check_if_date_of_price_is_available(prices, new_price):
    for price in prices:
            if price['date'] == new_price['date']:
                return False
    return True

def add_or_update_product(item):
    table = get_products_table()
    result = get_product(item['id'], table)

    if 'Item' in result:
        prices = result['Item']['prices']
        
        if check_if_date_of_price_is_available(prices, item['prices'][0]):
            prices.append(item['prices'][0])
            update_product_prices(item['id'], prices, table)
    else:
        add_product(item)

