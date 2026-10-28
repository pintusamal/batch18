from selenium import webdriver


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_chrome(self):
        self.driver= webdriver.Chrome()
        return self.driver

    def open_firefox(self):
        self.driver= webdriver.Firefox()
        return self.driver

    def open_ie(self):
        self.driver= webdriver.Ie()
        return self.driver

    def open_edge(self):
        self.driver= webdriver.Edge()
        return self.driver

    def open_browser(self, browser):
        if browser == "chrome":
            return  self.open_chrome()

        elif browser == "firefox":
            return self.open_firefox()

        elif browser == "ie":
            return self.open_ie()
        else:
            return self.open_edge()

    def open_url(self, url):
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()

    def close_window(self):
        self.driver.quit()

    def click_me(self, locator):
        element = self.get_web_element(locator)
        element.click()

    def type_word(self, locator, text):
        element = self.get_web_element(locator)
        element.send_keys(text)

    def get_web_element(self, locator):
        return self.driver.find_element(locator[0], locator[1])

