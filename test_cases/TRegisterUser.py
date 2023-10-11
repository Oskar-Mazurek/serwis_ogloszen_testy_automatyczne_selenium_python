import allure
from Template import Template
from selenium.webdriver.common.by import By


class TRegisterUser(Template):
    @allure.step("2. Rejestracja użytkownika poprzez formularz")
    def TRegisterUser(self, test_name):
        register_data = self.get_test_data(test_name)['user']
        for key in register_data.keys():
            input = self.driver.find_element(By.XPATH, f"//input[@name='{key}']")
            input.send_keys(register_data[key])
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-success']")
        self.driver.execute_script("arguments[0].click();", submit_button)
        success_info = self.driver.find_element(By.XPATH, "//div[@role = 'alert']")
        assert success_info.text == "Pomyślnie zarejestrowano!", "Nie udało się zarejestować"
