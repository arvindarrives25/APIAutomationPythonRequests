import pytest

from helpers.helper_request import RequestsHelper
from test_cases.test_base import TestBase


class TestSingleUsers(TestBase):
    single_users_end_point = "api/users/2"

    """Sample test case for get request, to test single user"""

    @pytest.mark.regression_test
    @pytest.mark.my_test_suite
    def test_single_users(self):
        obj = RequestsHelper()
        output = obj.helper_get_request(self.single_users_end_point, 200)
        errors = []
        if not output["support"]["url"] == "https://reqres.in/#support-heading":
            errors.append("an error message")
        if not output["support"]["text"] == "To keep ReqRes free, contributions towards server costs are appreciated!":
            errors.append("an other error message")
        if not output["data"]["id"] == 2:
            errors.append("an other error message")
        if not output["data"]["email"] == "janet.weaver@reqres.in":
            errors.append("an other error message")
        if not output["data"]["first_name"] == "Janet":
            errors.append("an other error message")
        if not output["data"]["last_name"] == "Weaver":
            errors.append("an other error message")
        if not output["data"]["avatar"] == "https://reqres.in/img/faces/2-image.jpg":
            errors.append("an other error message")
        assert not errors, "errors occurred:\n{}".format("\n".join(errors))