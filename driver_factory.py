from selenium import webdriver
from os import environ


class CreateDriver:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_driver'):
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            cls._driver = super(CreateDriver, cls).__new__(cls, *args, **kwargs)
            cls._driver = webdriver.Chrome(chrome_options=options, executable_path=environ[r"CHROMEDRIVER"])  # put into env variable

        return cls._driver
