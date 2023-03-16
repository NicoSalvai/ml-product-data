from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


def get_chrome_driver(explorer, headless, argument) -> WebDriver:
    options = ChromeOptions()
    options.headless = headless
    if argument and argument.strip():
        options.add_argument(argument)

    driver = Chrome(options=options)
    return driver


def get_local_chrome_full_screen() -> WebDriver:
    return get_chrome_driver(explorer='Chrome', headless=False, argument="--window-size=1920,1200")
