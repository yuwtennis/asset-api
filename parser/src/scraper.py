
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
Abstraction class defines function for scraping
"""

class Scraper:

    def __init__(self, browser, mode='--headless'):

      chrome_options = Options() 
      chrome_options.add_argument(mode)

      self._driver = webdriver.Chrome(options=chrome_options)

    # This will be overwritten
    def parse(self):
        pass

    # This will be overwritten
    def store(self):
        pass
