from selenium.webdriver.common.by import By


class Purchase_page:
    country = (By.ID, "country")
    checkbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
    confirm_button = (By.CSS_SELECTOR, "input[class*='btn-success']")
    success_message = (By.CSS_SELECTOR, "div[class *='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def enter_country(self):
        return self.driver.find_element(*Purchase_page.country)

    def click_checkbox(self):
        return self.driver.find_element(*Purchase_page.checkbox)

    def click_confirm(self):
        return self.driver.find_element(*Purchase_page.confirm_button)

    def grab_success_message(self):
        return self.driver.find_element(*Purchase_page.success_message)