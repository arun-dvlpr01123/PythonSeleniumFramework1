from selenium.webdriver.common.by import By

from page_objects.purchase_page import Purchase_page


class Confirm_page:
    phone_name = (By.XPATH, "//div[@class='media-body']/h4/a")
    confirm_checkout_button = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def get_phone_name(self):
        return self.driver.find_element(*Confirm_page.phone_name)

    def click_confirm_checkout(self):
        self.driver.find_element(*Confirm_page.confirm_checkout_button).click()
        purchase_page = Purchase_page(self.driver)
        return purchase_page
