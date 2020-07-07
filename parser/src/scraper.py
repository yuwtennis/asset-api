
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
Abstraction class defines function for scraping
"""

class Scraper:

    def __init__(self, mode='--headless'):

      chrome_options = Options() 
      chrome_options.add_argument(mode)

      self.driver = webdriver.Chrome(options=chrome_options)
