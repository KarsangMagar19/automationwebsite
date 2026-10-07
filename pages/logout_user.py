from playwright.sync_api import expect
username = "manish"
class LogoutUser:
    email = "manis@gmail.com"
    password = "password"

    def __init__(self, page):
        self.page = page

    def open_home_page(self):
        self.page.goto("https://www.automationexercise.com")
        expect(self.page).to_have_title("Automation Exercise")

    def click_login_link(self):
        # Click Signup / Login first
        self.page.get_by_role("link", name="Signup / Login").click()
        expect(
            self.page.get_by_role(
                "heading",
                name="Login to your account"
            )
        ).to_be_visible()
        
    def enter_login_credentials(self):
        self.page.locator('[data-qa="login-email"]').fill(self.email)
        self.page.locator('[data-qa="login-password"]').fill(self.password)
        self.page.locator('[data-qa="login-button"]').click()
        expect(
            self.page.get_by_text(
                f"Logged in as {username}",
                exact=False
            )
        ).to_be_visible()
    def logout(self):
        self.page.get_by_role("link", name="Logout").click()
        expect(self.page).to_have_url("https://www.automationexercise.com/login")
        self.page.wait_for_timeout(5000)
    def close_browser(self):
        self.page.close()
        