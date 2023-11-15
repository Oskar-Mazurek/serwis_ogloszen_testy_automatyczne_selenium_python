import allure
import pytest

from test_cases.TEnterLogin import TEnterLogin
from test_cases.TLoginUser import TLoginUser

from test_cases.TEnterRegistration import TEnterRegistration
from test_cases.TRegisterUser import TRegisterUser

from test_cases.TAdAddition import TAdAddition
from test_cases.TAdAddition2 import TAdAddition2

from test_cases.TAdSearch import TAdSearch1
from test_cases.TAdSearch2 import TAdSearch2

from test_cases.TAdDelete1 import TAdDelete1
from test_cases.TAdDelete2 import TAdDelete2
from test_cases.TAdDelete3 import TAdDelete3


# cykl testowy 1
class TestUserRegister(TEnterRegistration, TRegisterUser):
    def test(self):
        with allure.step("Test automatyczny funkcjonalności rejestracji użytkownika"):
            test_name = __class__.__qualname__
            self.TEnterRegistration(test_name)
            self.TRegisterUser(test_name)


# cykl testowy 2
class TestUserLogin(TEnterLogin, TLoginUser):
    def test(self):
        with allure.step("Test automatyczny funkcjonalności logowania użytkownika"):
            test_name = __class__.__qualname__
            self.TEnterLogin(test_name)
            self.TLoginUser(test_name)


# cykl testowy 3
class TestAdAddition(TAdAddition, TAdAddition2):
    def test(self):
        with allure.step("Test automatyczny funkcjonalności dodawania ogłoszeń"):
            test_name = __class__.__qualname__
            self.TAdAddition(test_name)
            self.TAdAddition2(test_name)


# cykl testowy 4
class TestAdSearch(TAdSearch1, TAdSearch2):
    def test(self):
        with allure.step("Test automatyczny funkcjonalności wyszukiwania ogłoszenia"):
            test_name = __class__.__qualname__
            self.TAdSearch1(test_name)
            self.TAdSearch2(test_name)


# cykl testowy 5
class TestAdDelete(TAdDelete1, TAdDelete2, TAdDelete3):
    def test(self):
        with allure.step("Test automatyczny funkcjonalności usuwania ogłoszenia"):
            test_name = __class__.__qualname__
            ad_selector = self.TAdDelete1(test_name)
            delete_prompt_selector = self.TAdDelete2(test_name, ad_selector)
            self.TAdDelete3(test_name, delete_prompt_selector)
