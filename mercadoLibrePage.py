import csv
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner

class MercadoLibre(object):

    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://www.mercadolibre.com/'

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(
        EC.element_to_be_clickable(By.ID ,'PE')
        )
        return True

    def open(self):
        self._driver.get(self._url)

    def select_country(self):
        select = self._driver.find_element(By.ID, 'PE').click()

    @property
    def keyword(self):
        input_field = self._driver.find_element(By.NAME, 'as_word')
        return input_field.get_attribute('value')

    def type_search(self, keyword):
        input_field = self._driver.find_element(By.NAME, 'as_word')
        input_field.clear()
        input_field.send_keys(keyword)

    def click_submit(self):
        input_field = self._driver.find_element(By.NAME, 'as_word')
        input_field.submit()

    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()

    def accept_cookies(self):
        click_cookies = self._driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/button[1]')
        click_cookies.click()

    def filter_new(self):
        click_new_products = self._driver.find_element(By.CSS_SELECTOR, '#root-app > div > div.ui-search-main.ui-search-main--only-products.ui-search-main--with-topkeywords.shops__search-main > aside > section > div:nth-child(5) > ul > li:nth-child(1) > a')
        click_new_products.click()
        
    def filter_location(self):
        click_location = self._driver.find_element(By.CSS_SELECTOR, '#root-app > div > div.ui-search-main.ui-search-main--only-products.ui-search-main--with-topkeywords.shops__search-main > aside > section.ui-search-filter-groups.shops__filter-groups > div:nth-child(6) > ul > li:nth-child(1) > a')
        click_location.click()
        
    def sort_by(self):

        click_sort_by = self._driver.find_element(By.XPATH, '/html/body/main/div/div[2]/section/div[2]/div/div/div/div[2]/div/div/button')
        click_sort_by.click()


        click_great_price = self._driver.find_element(By.CSS_SELECTOR, '#andes-dropdown-más-relevantes-list-option-price_desc > div > div > span')
        click_great_price.click()

    def get_names(self):

        names=[]
        for i in range(6):
            name= self._driver.find_element(By.XPATH, f'/html/body/main/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2')
            names.append(name.text)

        return names

    def get_prices(self):

        prices = []
        for i in range(6):
            price= self._driver.find_element(By.XPATH, f'/html/body/main/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]')
            prices.append(price.text)

        return prices

    def dict_names_prices(self):
        k = self.get_names()
        v = self.get_prices()
        my_dict = dict(zip(k,v))
        return my_dict

    def dict_to_csv(self):

        dictionary = self.dict_names_prices()
        with open('name_prices_products.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Price'])
            for key, value in dictionary.items():
                writer.writerow([key, value])



if __name__ == '__main__':
    unittest.main( verbosity= 2,
    testRunner = HTMLTestRunner(output = 'Reportotes', report_name = 'popup_report'))