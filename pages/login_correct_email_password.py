from playwright.sync_api import expect


username = "manish"


class LoginCorrectEmailPassword:

    def __init__(self, page):
        self.page = page
        self.email = "manis@gmail.com"
        self.password = "password"

    def open_home_page(self):
        self.page.goto("https://www.automationexercise.com")
        expect(self.page).to_have_title("Automation Exercise")

    def click_login_link(self):
        # Click Signup / Login first
        self.page.get_by_role("link", name="Signup / Login").click()

        # Verify login heading
        expect(
            self.page.get_by_role(
                "heading",
                name="Login to your account"
            )
        ).to_be_visible()

    def fill_login_form(self):
        self.page.locator('[data-qa="login-email"]').fill(self.email)
        self.page.locator('[data-qa="login-password"]').fill(self.password)
        self.page.locator('[data-qa="login-button"]').click()

        # Verify logged-in username
        expect(
            self.page.get_by_text(
                f"Logged in as {username}",
                exact=False
            )
        ).to_be_visible()

    def close_browser(self):
        self.page.close()

    