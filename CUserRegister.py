from test_cases.TEnterRegistration import TEnterRegistration
from test_cases.TRegisterUser import TRegisterUser
import allure


class TestUserRegister(TEnterRegistration, TRegisterUser):
    def test(self):
        test_name = __class__.__qualname__
        self.TEnterRegistration(test_name)
        self.TRegisterUser(test_name)
