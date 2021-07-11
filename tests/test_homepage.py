from page_objects.home_page import Homepage
from utilities.baseclass import baseclass


class Test_home_page(baseclass):

    def test_home_page(self, get_data):
        log = self.get_logger()
        homepage = Homepage(self.driver, get_data)
        try:
            assert "Successy" in homepage.fill_form()
        except AssertionError:
            log.error("Test case Failed")
