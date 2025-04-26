import pytest
from .base import HomePageBaseFunctionalTest


@pytest.mark.functional_test
class HomePageTest(HomePageBaseFunctionalTest):
    def test_home_page(self):
        self.browser.get(self.live_server_url)
