import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyunitreport import HTMLTestRunner
from mercadoLibrePage import MercadoLibre

class MercadoTest(unittest.TestCase):   

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.maximize_window()
        

    def test_search(self):
        mercado_libre = MercadoLibre(self.driver)
        mercado_libre.open()
        mercado_libre.select_country()
        mercado_libre.search('Play Station 4')
        mercado_libre.accept_cookies()
        mercado_libre.filter_new()
        mercado_libre.filter_location()
        mercado_libre.sort_by()
        mercado_libre.dict_names_prices()
        mercado_libre.dict_to_csv()


    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main( verbosity= 2,
    testRunner = HTMLTestRunner(output = 'Reportotes', report_name = 'popup_report'))