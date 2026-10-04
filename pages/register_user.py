class RegisterUser:
    def __init__(self, page):
        self.page = page

    def open_home_page(self):
        self.page.goto("https://www.automationexercise.com")

    def click_login_link(self):
        self.page.get_by_role("link", name=" Signup / Login").click()

    def fill_signup_form(self, name, email):
        self.page.locator('[data-qa="signup-name"]').fill(name)
        self.page.locator('[data-qa="signup-email"]').fill(email)
        self.page.locator('[data-qa="signup-button"]').click()

    def close_browser(self):
        self.page.close()

    


    


    