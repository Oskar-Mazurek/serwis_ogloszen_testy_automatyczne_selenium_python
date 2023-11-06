from Template import Template
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import allure


class TEnterRegistration(Template):
    @allure.step("1. Wejście na stronę i przejście do rejestracji")
    def TEnterRegistration(self, test_name):
        url = self.get_test_data(test_name)['url']
        self.driver.get(url)
        register_button = self.driver.find_element(By.XPATH, "//a[text()='Rejestracja']")
        register_button.click()
        register_header = self.driver.find_element(By.XPATH, "//div[@class='card-header'and text()='Rejestracja']")
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert register_header.text == 'Rejestracja', "Brak formularza z nagłówkiem Rejestracja"
