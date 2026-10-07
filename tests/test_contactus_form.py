from playwright._impl import _page
from pages.contactus_form import ContactUsForm
import pytest


class TestContactUsForm:
    def test_contactus_form(self, page):
        contact_us_form = ContactUsForm(page)
        contact_us_form.open_home_page()
        contact_us_form.click_contact_us()
        contact_us_form.fill_contact_form()
        contact_us_form.submit_and_verify()
        contact_us_form.click_home_button()
        contact_us_form.close_browser()
