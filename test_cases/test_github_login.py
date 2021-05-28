import pytest
import requests

from helpers.helper_auth import AuthHelper
from test_cases.test_base import TestBase
from utilities.configurations import get_config


class TestGITHUBAuth(TestBase):
    url = get_config()['GIT']['url']
    main_url = url+'user'
    s = requests.session()

    """Test case for post request"""
    @pytest.mark.regression_test
    @pytest.mark.my_test_suite
    def test_create_user(self):
        at = AuthHelper()
        res = self.s.get(self.main_url, auth=at.get_auth())
        assert res.status_code == 200, "Failed because status is not 200"
        assert res.json()['login'] == get_config()['GIT']['user'], "Failed because incorrect username"
