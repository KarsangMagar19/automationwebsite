from playwright.sync_api import expect

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
        
    def enter_login_credentials(self):
        self.page.locator('[data-qa="login-email"]').fill(self.email)
        self.page.locator('[data-qa="login-password"]').fill(self.password)
        self.page.locator('[data-qa="login-button"]').click()
    def logout(self):
        self.page.get_by_role("link", name="Logout").click()
        expect(self.page).to_have_url("https://www.automationexercise.com/login")
    def close_browser(self):
        self.page.close()
        