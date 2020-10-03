
import Scraper

class NomuraSec(Scraper):

    FORMAT     = '{}'
    STR_LOGOUT = 'ログアウト'

    def __init__(self, **kwargs):

        self._url         = kwargs['url']
        self._branch_code = kwargs['branch_code']
        self._account_num = kwargs['account_num']
        self._secret      = kwargs['secret']

    def run(self):
        self._access(self._url)
        self._login(self._branch_code, self._account_num, self._secret)
        self._logout(STR_LOGOUT)

    def _access(self, url):
        super().access(url)

    """ Override super class """
    def _login(self, branch_code, account_num, secret):
        btnCode       = driver.find_element_by_name('btnCd').send_keys(branch_code)
        kuzNo         = driver.find_element_by_name('kuzNo').send_keys(account_num)
        gnziLoginPswd = driver.find_element_by_name('gnziLoginPswd').send_keys(secret)

        driver.find_element_by_name('buttonLogin').click()

    """ Override super class """
    def _scrape(self):
        dd          = driver.find_element_by_class_name('ct-top-asset-summary-row')
        table       = dd.find_element_by_class_name('asset-summary-data')
        total_asset = table.find_element_by_xpath('//tbody/tr[1]/td').text
        profit      = table.find_element_by_xpath('//tbody/tr[2]/td').text

        mrf_remain  = dd.find_element_by_xpath('//div/div/p[2]').text

        date = datetime.datetime.utcnow().isoformat()

        return '{date},{total_asset},{profit},{mrf_remain}'

    def _logout(self, logout_str):
        super().logout(logout_str)
