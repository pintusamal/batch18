from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class DashBoardPage(BasePage):
    DASHBOARD_TXT = (By.XPATH, '//h6[text()="Dashboard"]')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver= driver

    def fetch_dashboard_text(self):
        return self.fetch_text(self.DASHBOARD_TXT)