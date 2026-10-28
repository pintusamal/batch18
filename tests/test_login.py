import pytest

from Pages.login_page import LoginPage
from util.common_funtions import read_json_data


class TestLogin:


    @pytest.mark.usefixtures("open_application")
    def test_validate_login_functionality(self):
        login_page  = LoginPage(self.driver)
        usename = read_json_data("username")
        password = read_json_data("password")
        login_page.login(usename , password)
