import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
from elasticsearch import Elasticsearch

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://hometrade.nomura.co.jp/web/mfIndexWebAction.do')

btnCode       = driver.find_element_by_name('btnCd').send_keys(os.getenv('NOMURA_SEC_BRANCH_CODE'))
kuzNo         = driver.find_element_by_name('kuzNo').send_keys(os.getenv('NOMURA_SEC_ACCOUNT_NUM'))
gnziLoginPswd = driver.find_element_by_name('gnziLoginPswd').send_keys(os.getenv('NOMURA_SEC_SECRET'))

driver.find_element_by_name('buttonLogin').click()

dd          = driver.find_element_by_class_name('ct-top-asset-summary-row')
table       = dd.find_element_by_class_name('asset-summary-data')
total_asset = table.find_element_by_xpath('//tbody/tr[1]/td').text
profit      = table.find_element_by_xpath('//tbody/tr[2]/td').text

mrf_remain  = dd.find_element_by_xpath('//div/div/p[2]').text
date = datetime.datetime.utcnow().isoformat()+'Z'

total_asset = total_asset.replace('円', '').replace(',', '')
profit = profit.replace('円', '').replace(',', '').replace('+', '')
mrf_remain = mrf_remain.replace('円', '').replace(',', '')

print(f'{date},{total_asset},{profit},{mrf_remain}')

driver.find_element_by_link_text('ログアウト').click()
driver.quit()

es = Elasticsearch(hosts=['localhost:19200'])

doc = {"total_asset": int(total_asset), "profit": int(profit), "mrf_remain": int(mrf_remain), "created_on": date }

es.index(index='nomura-sec', body=doc)
