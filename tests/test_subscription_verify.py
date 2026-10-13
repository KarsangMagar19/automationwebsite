from pages.subscription_verification import SubscriptionVerification


class TestSubscriptionVerify:
    def test_subscription_verify(self, page):
        subscription_verification = SubscriptionVerification(page)
        subscription_verification.verify_homePage()
        subscription_verification.scrollDown()
        subscription_verification.Enter_email()
        subscription_verification.click_subscribe()
        subscription_verification.verify_subscription()
