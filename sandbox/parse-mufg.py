import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from elasticsearch import Elasticsearch
import datetime

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://entry11.bk.mufg.jp/ibg/dfw/APLIN/loginib/login?_TRANID=AA000_001')

driver.find_element_by_name('KEIYAKU_NO').send_keys(os.getenv('MUFG_ACCOUNT_NUM'))
driver.find_element_by_name('PASSWORD').send_keys(os.getenv('MUFG_SECRET'))

driver.find_element_by_class_name('gonext').click()
driver.find_element_by_xpath('//div[@class="card-body"]/section[5]/a[3]').click()
driver.find_element_by_xpath('//div[@id="contents"]/div/div[3]/div/div/div/div/ul/li[1]').click()
driver.find_element_by_xpath('//input[@value="選択"]').click()

term_deposit = driver.find_element_by_xpath('//div[@class="serviceContents"]/div[3]/table/tbody/tr/td[5]').text
term_deposit = term_deposit.replace('円', '').replace(',', '')

date = datetime.datetime.utcnow().isoformat() + 'Z'

print(f'{term_deposit}')

driver.find_element_by_link_text('ログアウト').click()
driver.quit()

es = Elasticsearch(hosts=['localhost:19200'])
doc = {"term_deposit": int(term_deposit), "created_on": date }
es.index(index='mufg', body=doc)

