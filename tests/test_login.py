import pytest

from Pages.dashboard_page import DashBoardPage
from Pages.login_page import LoginPage
from util.common_funtions import read_json_data


class TestLogin:


    @pytest.mark.usefixtures("open_application")
    def test_validate_login_functionality(self):
        login_page  = LoginPage(self.driver)
        usename = read_json_data("username")
        password = read_json_data("password")
        login_page.login(usename , password)
        exp_dashboard_text = read_json_data("dashboard_txt")
        dashboard_page = DashBoardPage(self.driver)
        act_dashboard_text = dashboard_page.fetch_dashboard_text()
        assert act_dashboard_text == exp_dashboard_text


    @pytest.mark.usefixtures("open_application")
    def test_verify_forgot_password_functionality(self):
        login_page  = LoginPage(self.driver)
        login_page.click_on_forgot_pass_btn()
        reset_username = read_json_data("reset_username")
        login_page.reset_password(reset_username)

