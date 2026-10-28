from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.XPATH, '//input[@id="username"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BTN = (By.XPATH, '//input[@id="login-button"]')

    def __init__(self, driver):
        self.driver= driver
        super().__init__(self.driver)


    def login(self, usrname, pwd):
        self.type_word(self.USERNAME , usrname)
        self.type_word(self.PASSWORD , pwd)
        self.click_me(self.LOGIN_BTN )





