from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.XPATH, '//input[@name="username"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    LOGIN_BTN = (By.XPATH, '//button[@type="submit"]')
    FORGOT_PASS_BTN = (By.XPATH, '//p[text()="Forgot your password? "]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver= driver



    def login(self, usrname, pwd):
        self.type_word(self.USERNAME , usrname)
        self.type_word(self.PASSWORD , pwd)
        self.click_me(self.LOGIN_BTN )

    def click_on_forgot_pass_btn(self):
        self.click_me(self.FORGOT_PASS_BTN)

    def reset_password(self, username_txt):
        self.type_word(self.USERNAME, username_txt)
        self.click_me(self.LOGIN_BTN)





