from selenium.webdriver.common.by import By
from config.selenium.configs import get_chrome_from_env
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
import datetime
from selenium.common.exceptions import NoSuchElementException

def process_search(url, debug_process_only_one=False):
    driver = get_chrome_from_env()
    driver.get(url)

    button = driver.find_element(By.XPATH, "//button[@type='button']")
    button.click()

    elements_list = driver.find_elements(
        By.XPATH, "//ol[contains(@class, 'ui-search-layout')]/li")

    links_list = []
    for result in elements_list:
        link = result.find_element(
            By.XPATH, ".//a[contains(@class, 'shops__items-group-details')]").get_attribute('href')
        links_list.append(link)
        if debug_process_only_one:
            break

    products = []
    for link in links_list:
        products.append(process_product(link, driver))

    return products


def process_product(url, driver: WebDriver = None):
    if driver is None:
        driver = get_chrome_from_env()

    driver.get(url)
    sleep(2)
    link = driver.find_element(
        By.XPATH, "//input[@name='parent_url']").get_attribute('value')
    title = driver.find_element(
        By.XPATH, "//h1[@class='ui-pdp-title']").get_attribute('innerHTML')
    price = driver.find_element(
        By.XPATH, "//div[contains(@class,'ui-pdp-price')]")
    price_symbol = price.find_element(
        By.XPATH, ".//span[contains(@class, 'andes-money-amount__currency-symbol')]").get_attribute('innerHTML')
    price_amount = price.find_element(
        By.XPATH, ".//span[contains(@class, 'andes-money-amount__fraction')]").get_attribute('innerHTML')
    image = driver.find_element(
        By.XPATH, "//img[contains(@class,'ui-pdp-image ui-pdp-gallery__figure__image')]").get_attribute('src')

    return {
        'link': link if link.startswith("https:") else "https://articulo.mercadolibre.com.ar" + link,
        'title': title,
        'prices': [
            {
                'price_symbol': price_symbol,
                'price_amount': price_amount,
                'date': datetime.date.today().strftime("%d-%m-%Y"),
                'pausado': False
            }
        ],
        'image': image
    }

def check_exists_by_xpath(xpath, driver: WebDriver = None) -> bool:
    if driver is None:
        driver = get_chrome_from_env()

    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def get_new_price_prouct(url, driver: WebDriver = None):
    if driver is None:
        driver = get_chrome_from_env()

    driver.get(url)
    sleep(2)
    
    pausado = check_exists_by_xpath(xpath="//div[text()='Publicación pausada']", driver=driver)
    price = driver.find_element(
        By.XPATH, "//div[contains(@class,'ui-pdp-price')]")
    price_symbol = price.find_element(
        By.XPATH, ".//span[contains(@class, 'andes-money-amount__currency-symbol')]").get_attribute('innerHTML')
    price_amount = price.find_element(
        By.XPATH, ".//span[contains(@class, 'andes-money-amount__fraction')]").get_attribute('innerHTML')

    return {
        'link': url,
        'prices': [
            {
                'price_symbol': price_symbol,
                'price_amount': price_amount,
                'date': datetime.date.today().strftime("%d-%m-%Y"),
                'pausado': pausado
            }
        ]
    }
        