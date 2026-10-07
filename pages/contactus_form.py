from playwright.sync_api import expect


class ContactUsForm:

    def __init__(self, page):
        self.page = page

    def open_home_page(self):
        self.page.goto("https://www.automationexercise.com")
        expect(self.page).to_have_title("Automation Exercise")

    def click_contact_us(self):
        self.page.get_by_role("link", name="Contact us").click()

        expect(self.page.get_by_role("heading", name="Get in Touch")).to_be_visible()

    def fill_contact_form(self):
        # Wait for all scripts (including the inline jQuery form handler) to load
        self.page.wait_for_load_state("domcontentloaded")

        self.page.locator("[data-qa='name']").fill("manish")
        self.page.locator("[data-qa='email']").fill("manis@gmail.com")
        self.page.locator("[data-qa='subject']").fill("hello")
        self.page.locator("[data-qa='message']").fill(
            "hello this is manish from automation test"
        )

        self.page.locator("input[type='file']").set_input_files(
            r"C:\Users\sagarmatha\Documents\C4_Container.puml.txt"
        )

    def submit_and_verify(self):
        # Ensure jQuery and the form submit handler are fully loaded
        self.page.wait_for_load_state("load")
        self.page.wait_for_function(
            "typeof jQuery !== 'undefined' && jQuery('#contact-us-form').length > 0"
        )

        # Handle confirmation popup
        def handle_dialog(dialog):
            print("Dialog type:", dialog.type)
            print("Dialog message:", dialog.message)
            dialog.accept()

        self.page.once("dialog", handle_dialog)

        # Submit form
        self.page.locator("[data-qa='submit-button']").click()

        # Verify success message
        success_message = self.page.locator("div.status.alert.alert-success")
        expect(success_message).to_be_visible(timeout=10000)
        expect(success_message).to_have_text(
            "Success! Your details have been submitted successfully."
        )
        self.page.wait_for_timeout(5000)
