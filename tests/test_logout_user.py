import pytest
from playwright.sync_api import expect
from pages.logout_user import LogoutUser

class TestLogoutUser:
    def test_logout_user(self, page):
        logout_user = LogoutUser(page)
        logout_user.open_home_page()
        logout_user.click_login_link()
        logout_user.enter_login_credentials()
        logout_user.logout()
        logout_user.close_browser()