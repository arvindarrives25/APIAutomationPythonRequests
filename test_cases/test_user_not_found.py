import pytest

from helpers.helper_request import RequestsHelper
from test_cases.test_base import TestBase


class TestSingleUsersNotFound(TestBase):
    single_users_not_found_end_point = "api/users/23"

    """Sample test case when there are no users"""
    @pytest.mark.smoke_test
    @pytest.mark.regression_test
    @pytest.mark.my_test_suite
    def test_single_users(self):
        obj = RequestsHelper()
        output = obj.helper_get_request(self.single_users_not_found_end_point)
        errors = []
        if not output.status_code == 404:
            errors.append("status_code is not 404")
        if not output.json() == {}:
            errors.append("Output payload is not {}")
        assert not errors, "errors occurred:\n{}".format("\n".join(errors))

