import requests
import json
import logging as logger

from utilities.configurations import get_config


class RequestsHelper:

    def __init__(self):
        self.base_url = get_config()['API']['base_url']
        self.s = requests.session()

    """This is a generic get method """
    def helper_get_request(self, endpoint, expected_status_code=None, payload=None, headers=None, timeout=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        try:
            res = requests.get(url=url, data=json.dumps(payload), headers=headers, timeout=timeout)
            res_json = res.json()
            assert res.status_code == expected_status_code, \
                "Actual status {} and Expected status {} are not same ".format(res.status_code, expected_status_code)
            logger.debug(f"GET API response: {res_json}")
            return res_json
        except json.decoder.JSONDecodeError:
            res_empty = requests.get(url=url)
            return res_empty

    """This is a generic post method """

    def helper_post_request(self, endpoint, expected_status_code, payload=None, headers=None, timeout=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        res = requests.post(url=url, data=json.dumps(payload), headers=headers, timeout=timeout)
        res_json = res.json()
        assert res.status_code == expected_status_code, \
            "Actual status {} and Expected status {} are not same ".format(res.status_code, expected_status_code)
        logger.debug(f"GET API response: {res_json}")
        return res_json

    """This is a generic put method """

    def helper_put_request(self, endpoint, expected_status_code, payload=None, headers=None, timeout=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        res = requests.put(url=url, data=json.dumps(payload), headers=headers, timeout=timeout)
        res_json = res.json()
        assert res.status_code == expected_status_code, \
            "Actual status {} and Expected status {} are not same ".format(res.status_code, expected_status_code)
        logger.debug(f"GET API response: {res_json}")
        return res_json

    """This is a generic patch method """

    def helper_patch_request(self, endpoint, expected_status_code, payload=None, headers=None, timeout=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        res = requests.patch(url=url, data=json.dumps(payload), headers=headers, timeout=timeout)
        res_json = res.json()
        assert res.status_code == expected_status_code, \
            "Actual status {} and Expected status {} are not same ".format(res.status_code, expected_status_code)
        logger.debug(f"GET API response: {res_json}")
        return res_json

    """This is a generic delete method """

    def helper_delete_request(self, endpoint, expected_status_code, payload=None, headers=None, timeout=None, auth=None):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        res = requests.delete(url=url, data=json.dumps(payload), headers=headers, timeout=timeout, auth=auth)
        res_json = res.json()
        assert res.status_code == expected_status_code, \
            "Actual status {} and Expected status {} are not same ".format(res.status_code, expected_status_code)
        logger.debug(f"GET API response: {res_json}")
        return res_json

#For debug puprpose only
# end = "api/users"
# print(RequestsHelper().helper_post_request(end, 201, create_user()))
