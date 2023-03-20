from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os


def get_chrome_driver(explorer, headless, argument) -> WebDriver:
    options = ChromeOptions()
    options.headless = headless
    if argument and argument.strip():
        options.add_argument(argument)

    driver_path = os.environ["driver_path"]
    print(driver_path)
    if driver_path is not None:
        return Chrome(driver_path, options=options)
    return Chrome(osoptions=options)

def get_chrome_from_env() -> WebDriver:
    headless = True if os.environ["headless"] == "True" else False
    argument = os.environ["argument"]
    explorer = os.environ["explorer"]
    return get_chrome_driver(explorer=explorer, headless=headless, argument=argument)
