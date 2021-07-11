from selenium.webdriver.common.by import By

from page_objects.confirm_page import Confirm_page


class Checkout_page():
    card_items = (By.CSS_SELECTOR, "div[class*='h-100']")
    phone_name = (By.XPATH, "div/h4/a")
    select_button = (By.XPATH, "div[2]/button")
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver


    def get_card_items(self):
        return self.driver.find_elements(*Checkout_page.card_items)

    def get_phone_name(self,item):

        return item.find_element(*Checkout_page.phone_name)

    def select_phone_item(self,item):
        item.find_element(*Checkout_page.select_button).click()

    def checkout_phone_item(self):
        self.driver.find_element(*Checkout_page.checkout_button).click()
        confirm_page = Confirm_page(self.driver)
        return confirm_page