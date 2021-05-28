import pytest

from helpers.helper_db_connection import DBConnectionHelper
from test_cases.test_base import TestBase


class TestCreatePayloadFromDB(TestBase):

    query1 = 'select * from program'
    tup1 = ("course", "code", "id", "Trainer")

    """Test case which will create dynamic payload from db table.
    The output will be a dictionary so finally can be used as payload for any API Operations
    This is just a poc and can be extend as per the use or requirement """
    @pytest.mark.smoke_test
    @pytest.mark.my_test_suite
    @pytest.mark.regression_test
    def test_create_dynamic_payload(self):
        obj = DBConnectionHelper.get_dynamic_payload(self.query1, self.tup1, 0)
        print(obj)
