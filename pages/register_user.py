from playwright.sync_api import expect
username="John Doe"
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
        self.page.wait_for_url("https://www.automationexercise.com/signup")
    def enter_account_details(self):
        self.page.locator('[for="id_gender1"]').check()
        self.page.get_by_role("textbox", name="password").fill("password")
        self.page.locator("#days").select_option("27")
        self.page.locator("#months").select_option("July")
        self.page.locator("#years").select_option("1990")
        self.page.get_by_role("checkbox",name="newsletter").check()
        self.page.locator("#optin").check()
        self.page.locator('[data-qa="first_name"]').fill("John")
        self.page.locator('[data-qa="last_name"]').fill("Doe")
        self.page.locator('[data-qa="company"]').fill("Company")
        self.page.locator("#address1").fill("123 Main St")
        self.page.locator("#address2").fill("123 Main St")
        self.page.get_by_role("combobox", name="country").select_option("United States")
        self.page.get_by_role("textbox", name="state").fill("California")
        self.page.get_by_role("textbox", name="city").fill("Los Angeles")
        self.page.locator("#zipcode").fill("12345")
        self.page.locator("#mobile_number").fill("1234567890")
        self.page.get_by_role("button",name="Create Account").click()
        self.page.wait_for_url("https://www.automationexercise.com/account_created")
        self.page.get_by_role("link", name="Continue").click()
        self.page.wait_for_url("https://www.automationexercise.com")
        self.page.wait_for_timeout(2000)
        expect(self.page.get_by_text(f"Logged in as {username}", exact=False)).to_be_visible()
        self.page.get_by_role("link", name="Delete Account").click()
        expect(self.page.get_by_text("Account Deleted!")).to_be_visible()
        self.page.get_by_role("link", name="Continue").click()
        self.page.wait_for_url("https://www.automationexercise.com")
        


    def close_browser(self):
        self.page.close()

    


    


    