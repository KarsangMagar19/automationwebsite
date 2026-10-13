from playwright.sync_api import Page, expect


class SubscriptionVerification:
    def __init__(self, page: Page):
        self.page = page
        self.goto_url = "https://www.automationexercise.com/"

    def verify_homePage(self):
        self.page.goto(self.goto_url)
        expect(self.page).to_have_url(self.goto_url)
        expect(self.page).to_have_title("Automation Exercise")

    def scrollDown(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def Enter_email(self):
        self.page.locator("#susbscribe_email").fill("email@gmail.com")
        self.page.wait_for_timeout(1000)

    def click_subscribe(self):
        self.page.locator("#subscribe").click()
        self.page.wait_for_timeout(1000)

    def verify_subscription(self):
        expect(self.page.locator("div.alert.alert-success")).to_contain_text(
            "You have been successfully subscribed!"
        )
