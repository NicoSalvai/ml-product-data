import scrapper as Scrapper
import persistence.dynamodb.products as Products


def process_complete_search(url, save, debug=False):
    search_results = Scrapper.process_search(url, debug)
    for item in search_results:
        if save:
            Products.add_or_update_product(item)
        else:
            print(item)


process_complete_search(url="https://listado.mercadolibre.com.ar/consolas-videojuegos/accesorios-consolas/xbox/xbox-series-x-s/joysticks/xbox_NoIndex_True#D[A:xbox,on]",
                        save=True,
                        debug=False
                        )
