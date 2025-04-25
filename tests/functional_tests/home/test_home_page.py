from base import HomePageBaseFunctionalTest


class HomePageTest(HomePageBaseFunctionalTest):
    def test_home_page(self):
        self.browser.get(self.live_server_url)
