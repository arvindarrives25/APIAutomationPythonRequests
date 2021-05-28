from utilities.configurations import get_config


class AuthHelper:

    @staticmethod
    def get_username():
        user = get_config()['GIT']['user']
        return user

    @staticmethod
    def get_password():
        password = get_config()['GIT']['access_token']
        return password

    def get_auth(self):
        return self.get_username(), self.get_password()
