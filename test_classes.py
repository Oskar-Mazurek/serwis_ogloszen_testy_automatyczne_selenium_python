import allure
import pytest

from test_cases.TEnterLogin import TEnterLogin
from test_cases.TLoginUser import TLoginUser

from test_cases.TEnterRegistration import TEnterRegistration
from test_cases.TRegisterUser import TRegisterUser


class TestUserRegister(TEnterRegistration, TRegisterUser):
    def test(self):
        test_name = __class__.__qualname__
        self.TEnterRegistration(test_name)
        self.TRegisterUser(test_name)


class TestUserLogin(TEnterLogin, TLoginUser):
    def test(self):
        test_name = __class__.__qualname__
        self.TEnterLogin(test_name)
        self.TLoginUser(test_name)
