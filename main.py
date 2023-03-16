import scrapper as Scrapper
import persistence.dynamodb.products as Products
from dotenv import load_dotenv
import os

def process_complete_search(url):
    search_results = Scrapper.process_search(url, True if os.environ["debug"] == "True" else False)
    for item in search_results:
        if True if os.environ["save"] == "True" else False:
            Products.add_or_update_product(item)
        else:
            print(item)


load_dotenv()
process_complete_search(url=os.environ["url"])