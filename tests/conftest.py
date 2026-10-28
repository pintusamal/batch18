import pytest
from selenium import webdriver

from Pages.base_page import BasePage
from util.common_funtions import read_json_data


@pytest.fixture(scope="function")
def open_application(request):
    browser = read_json_data("browser")  # firefox
    global driver

    base_page = BasePage(driver=None)
    base_page.open_browser(browser)

    url = read_json_data("url")
    base_page.open_url(url)

    base_page.maximize_window()
    request.cls.driver = driver
    yield
    base_page.close_window()
