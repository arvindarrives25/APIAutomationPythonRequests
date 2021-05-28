import pytest

from helpers.helper_request import RequestsHelper
from test_cases.test_base import TestBase


class TestListUsers(TestBase):
    list_users_end_point = "api/users?page=2"

    """Sample test case for get request"""

    @pytest.mark.smoke_test
    @pytest.mark.my_test_suite
    @pytest.mark.regression_test
    def test_list_users(self):
        obj = RequestsHelper()
        output = obj.helper_get_request(self.list_users_end_point, 200)
        errors = []
        if not output["data"][0]["id"] == 7:
            errors.append("an error message")
        if not output["data"][0]["email"] == "michael.lawson@reqres.in":
            errors.append("an other error message")
        if not output["data"][0]["first_name"] == "Michael":
            errors.append("an other error message")
        if not output["data"][0]["last_name"] == "Lawson":
            errors.append("an other error message")
        assert not errors, "errors occurred:\n{}".format("\n".join(errors))
