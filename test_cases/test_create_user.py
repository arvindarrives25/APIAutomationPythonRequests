import pytest

from data.create_user_data import create_user
from helpers.helper_request import RequestsHelper
from test_cases.test_base import TestBase


class TestCreateUser(TestBase):
    create_user = "api/users"

    """Test case for post request"""
    @pytest.mark.smoke_test
    @pytest.mark.my_test_suite
    @pytest.mark.regression_test
    def test_create_user(self):
        obj = RequestsHelper()
        output = obj.helper_post_request(self.create_user, 201, create_user())
        errors = []
        if not output["name"] == "morpheus":
            errors.append("Name is not morpheus")
        if not output["job"] == "leader":
            errors.append("Job is not leader")
        assert not errors, "errors occurred:\n{}".format("\n".join(errors))
        return [output["id"], output["createdAt"]]