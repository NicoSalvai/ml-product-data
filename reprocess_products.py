import scrapper as Scrapper
import persistence.dynamodb.products as Products
from config.selenium.configs import get_chrome_from_env
from dotenv import load_dotenv
import os


def reprocess_products():
    products = Products.get_products()
    driver = get_chrome_from_env()
    for product in products:
        print(product)
        updatable_product = Scrapper.get_new_price_prouct(product['link'], driver)
        product["prices"] = updatable_product["prices"]
        if True if os.environ["save"] == "True" else False:
            Products.add_or_update_product(product)
        else:
            print(product)


load_dotenv()
reprocess_products()
