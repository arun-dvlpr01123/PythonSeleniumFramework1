
import pytest
from selenium import webdriver
import time

driver = None
from test_data.homepage_test_data import Homepage_test_data


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome or firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="/home/arun/selenium/chromedriver")

    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="/home/arun/selenium/geckodriver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.close()


@pytest.fixture(scope="class", params=Homepage_test_data.get_data_excel())
def get_data(request):
    return request.param


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
