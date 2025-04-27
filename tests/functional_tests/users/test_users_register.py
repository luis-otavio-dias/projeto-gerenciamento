import pytest
from .base import UserBaseFunctionalTest


@pytest.mark.functional_test
class UserResgisterTest(UserBaseFunctionalTest):
    def test_user_register(self):
        self.browser.get(self.live_server_url + "/users/register/")
