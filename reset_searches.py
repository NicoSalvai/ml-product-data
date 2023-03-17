import persistence.dynamodb.searches as Searches
from dotenv import load_dotenv

def process_searches_from_db():
    searches = Searches.get_searches(enabled=False)
    print(searches)
    for search in searches:
        Searches.update_search_enabled(search['id'], True)

load_dotenv()
process_searches_from_db()