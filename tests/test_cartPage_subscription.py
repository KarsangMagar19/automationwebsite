from pages.cartPage_subscription import CartPageSubscription


class TestCartPageSubscription:
    def test_cartPage_subscription(self, page):
        cartPage_subscription = CartPageSubscription(page)
        cartPage_subscription.verify_homePage()
        cartPage_subscription.click_cart()
        cartPage_subscription.scrollDown()
        cartPage_subscription.verify_subsciption_text()
        cartPage_subscription.Enter_email()
        cartPage_subscription.click_subscribe()
        cartPage_subscription.verify_subscription()
