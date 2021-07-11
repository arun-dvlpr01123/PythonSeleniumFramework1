
import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from page_objects.checkout_page import Checkout_page
from page_objects.confirm_page import Confirm_page
from page_objects.home_page import Homepage
from page_objects.purchase_page import Purchase_page
from utilities.baseclass import baseclass


class Test_one(baseclass):

    def test_e2e(self, setup):
        homepage = Homepage(self.driver)
        log = self.get_logger()

        log.info("Test case Starts here by opening the URL")

        checkout_page = homepage.shop_items()
        items = checkout_page.get_card_items()
        phone_name = ""
        for item in items:
            phone_name = checkout_page.get_phone_name(item).text
            log.info(phone_name)
            if "blackberry" in phone_name.lower():
                checkout_page.select_phone_item(item)
                log.info(phone_name + "match found")
                break
            else:
                log.info(phone_name + "did not match")
        confirm_page = checkout_page.checkout_phone_item()
        try:
            assert phone_name == confirm_page.get_phone_name().text.lower()

        except AssertionError:
            log.error(phone_name)
            log.error(confirm_page.get_phone_name().text.lower())
            log.error("Test Case Failed since name of item ordered does not match what is in checkout")

        else:
            print("Phone Name Validation passed")
            log.info("Successfully done shopping")
        purchase_page = confirm_page.click_confirm_checkout()
        purchase_page.enter_country().send_keys("uni")

        self.verify_link_text("United States of America").click()
        purchase_page.click_checkbox().click()
        purchase_page.click_confirm().click()
        success_message = purchase_page.grab_success_message().text

        try:
            assert "Success" in success_message.lower()
        except AssertionError:
            print("Test Case Failed success message not there")
            self.driver.get_screenshot_as_file("../screenshots/purchasefailure.png")
        else:
            print("Phone purchase validation passed")
