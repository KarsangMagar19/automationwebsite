from playwright.sync_api import expect
class RegisterExistingEmail:
    def __init__(self, page):
        self.page = page

    def open_home_page(self):
        self.page.goto("https://www.automationexercise.com")
        expect(self.page).to_have_title("Automation Exercise")
    
    def click_signup_login(self):
        self.page.get_by_role("link", name="Signup / Login").click()
        expect(self.page.get_by_role("heading", name="New User Signup!")).to_be_visible()
    
    def enter_signup_credentials(self):
        self.page.locator("[data-qa='signup-name']").fill("manish")
        self.page.locator("[data-qa='signup-email']").fill("manis@gmail.com")
        self.page.locator("[data-qa='signup-button']").click()
        expect(self.page.get_by_text("Email Address already exist!")).to_be_visible()
        self.page.wait_for_timeout(5000)
    def close_browser(self):
        self.page.close()