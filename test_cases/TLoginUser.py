import allure
from Template import Template
from selenium.webdriver.common.by import By


class TLoginUser(Template):
    @allure.step("2. Zalogowanie użytkownika poprzez formularz")
    def TLoginUser(self, test_name):
        login_user_data = self.get_test_data(test_name)['user']
        for key in login_user_data.keys():
            input_field = self.driver.find_element(By.XPATH, f"//input[@name='{key}']")
            input_field.send_keys(login_user_data[key])
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-success']")
        self.driver.execute_script("arguments[0].click();", submit_button)
        success_info = self.driver.find_element(By.XPATH, "//div[@role = 'alert']")
        assert success_info.text == "Udało się zalogować", "Nie udało się zalogować"
