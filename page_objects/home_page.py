import time

from selenium.webdriver.common.by import By

from page_objects.checkout_page import Checkout_page
from utilities.baseclass import baseclass


class Homepage(baseclass):

    def __init__(self, driver, *args):
        self.driver = driver
        for ar in args:
            self.name_data = ar["name"]
            self.email_data = ar["email"]
            self.gender_data = ar["gender"]

    shop = (By.XPATH, "//ul[@class='navbar-nav']/li[2]/a")
    name = (By.XPATH, "//div[@class='form-group'][1]/input[1]")
    email = (By.XPATH, "//div[@class='form-group'][2]/input[1]")
    password = (By.XPATH, "//div[@class='form-group'][3]/input[1]")
    i_love_icecream = (By.CSS_SELECTOR, "#exampleCheck1")
    gender_dropdown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    employment_status = (By.CSS_SELECTOR, "#inlineRadio1")
    submit_button = (By.CSS_SELECTOR, "input[class*='btn-success']")
    success_message = (By.CSS_SELECTOR, "div[class*=alert-success]")

    def shop_items(self):
        time.sleep(1)
        shop_link = self.verify_element_clickable(Homepage.shop)
        shop_link.click()
        checkout_page = Checkout_page(self.driver)
        return checkout_page

    def fill_form(self):
        self.driver.refresh()
        log = self.get_logger()
        self.driver.find_element(*Homepage.name).send_keys(self.name_data)
        self.driver.find_element(*Homepage.email).send_keys(self.email_data)
        self.driver.find_element(*Homepage.password).send_keys("Apple123")
        self.driver.find_element(*Homepage.i_love_icecream).click()
        log.info("I love ice cream checkbox clicked")
        dropdown_element = self.driver.find_element(*Homepage.gender_dropdown)
        self.select_dropdown(dropdown_element, self.gender_data)
        self.driver.find_element(*Homepage.employment_status).click()
        self.driver.find_element(*Homepage.submit_button).click()
        success_text = self.driver.find_element(*Homepage.success_message).text
        log.info("Succes Message captured")
        return success_text
