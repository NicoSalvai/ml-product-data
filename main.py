from dotenv import load_dotenv
from process_searches import process_searches
from reprocess_products import reprocess_products

load_dotenv()
reprocess_products()
process_searches()