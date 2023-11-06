import time

import allure
from Template import Template
from selenium.webdriver.common.by import By


class TAdAddition2(Template):
    @allure.step("2. Dodanie ogłoszenia poprzez formularz")
    def TAdAddition2(self, test_name):
        ad_data = self.get_test_data(test_name)['adData']
        for key in ad_data.keys():
            input_field = self.driver.find_element(By.XPATH, f"//*[@name='{key}']")
            input_field.send_keys(ad_data[key])
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-success']")
        self.driver.execute_script("arguments[0].click();", submit_button)
        success_info = self.driver.find_element(By.XPATH, "//div[@role = 'alert']")
        assert success_info.text == "Dodano ogłoszenie!", "Nie udało się dodać ogłoszenia"
