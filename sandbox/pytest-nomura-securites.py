import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://hometrade.nomura.co.jp/web/mfIndexWebAction.do')

btnCode = driver.find_element_by_name('btnCd')
kuzNo   = driver.find_element_by_name('kuzNo')
gnziLoginPswd = driver.find_element_by_name('gnziLoginPswd')

btnCode.send_keys(os.getenv('BTNCODE'))
kuzNo.send_keys(os.getenv('KUZNO'))
gnziLoginPswd.send_keys('GNZILOGINPSWD')
driver.find_element_by_name('buttonLogin').click()

# TODO
# Need to parse table
table = find_element_by_class_name('asset-summary-data')

# TODO
# Need to click logout

# TODO
# Need to quit browser
