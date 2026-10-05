from conftest import page
from playwright.sync_api import expect

username = "manish"


class LoginWithInvalidCredentials:
    email = "manish123@cmail.com"
    password = "password"

    def __init__(self, page):
        self.page = page

    def open_home_page(self):
        self.page.goto("https://www.automationexercise.com")
        expect(self.page).to_have_title("Automation Exercise")

    def click_login_link(self):
        self.page.get_by_role("link", name=" Signup / Login").click()

    def fill_login_form(self):
        expect(
            self.page.get_by_role("heading", name="Login to your account")
        ).to_be_visible()
        self.page.locator('[data-qa="login-email"]').fill(self.email)
        self.page.locator('[data-qa="login-password"]').fill(self.password)
        self.page.locator('[data-qa="login-button"]').click()
        expect(
            self.page.get_by_text("Your email or password is incorrect!")
        ).to_be_visible()
        self.page.wait_for_timeout(2000)

    def close_browser(self):
        self.page.close()
