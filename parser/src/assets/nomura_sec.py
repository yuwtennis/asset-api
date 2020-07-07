
from scraper import Scraper

class NomuraSec(Scraper):

    FORMAT = '{}'

    def __init__(self, **kwargs):

        self._url = kwargs['url']
        self._branch_code = 

    def parse(self):

        self.driver.get(url)

        btnCode       = driver.find_element_by_name('btnCd').send_keys(os.getenv('NOMURA_SEC_BRANCH_CODE'))
        kuzNo         = driver.find_element_by_name('kuzNo').send_keys(os.getenv('NOMURA_SEC_ACCOUNT_NUM'))
        gnziLoginPswd = driver.find_element_by_name('gnziLoginPswd').send_keys(os.getenv('NOMURA_SEC_SECRET'))

        driver.find_element_by_name('buttonLogin').click()

        dd          = driver.find_element_by_class_name('ct-top-asset-summary-row')
        table       = dd.find_element_by_class_name('asset-summary-data')
        total_asset = table.find_element_by_xpath('//tbody/tr[1]/td').text
        profit      = table.find_element_by_xpath('//tbody/tr[2]/td').text

        mrf_remain  = dd.find_element_by_xpath('//div/div/p[2]').text

        date = datetime.datetime.utcnow().isoformat()

        return '{date},{total_asset},{profit},{mrf_remain}')

    def logout(self)
        driver.find_element_by_link_text('ログアウト').click()
        driver.quit()

