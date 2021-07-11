import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup", "get_data")
class baseclass:
    def verify_link_text(self, text):
        wait1 = WebDriverWait(self.driver, 10)
        element = wait1.until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
        return element

    def verify_element_clickable(self, input_element):
        wait1 = WebDriverWait(self.driver, 10)
        element = wait1.until(
            expected_conditions.visibility_of_element_located(input_element))
        return element

    def select_dropdown(self, locator, text):
        dropdown = Select(locator).select_by_visible_text(text)

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('../utilities/test_logs.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
