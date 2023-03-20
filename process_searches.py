import scrapper as Scrapper
import persistence.dynamodb.products as Products
import persistence.dynamodb.searches as Searches
import os


def process_complete_search(search):
    search_results = Scrapper.process_search(
        search['link'], True if os.environ["debug"] == "True" else False)
    for item in search_results:
        item['search_id'] = search['id']
        item['tags'] = search['tags']

        if True if os.environ["save"] == "True" else False:
            Products.add_or_update_product(item)
        else:
            print(item)


def process_searches():
    searches = Searches.get_searches()
    for search in searches:
        process_complete_search(search)
        Searches.update_search_enabled(search['id'], False)