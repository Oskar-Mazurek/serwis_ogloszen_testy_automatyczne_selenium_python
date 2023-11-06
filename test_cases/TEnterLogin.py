import allure
from Template import Template
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


class TEnterLogin(Template):
    @allure.step("1. Wejście na stronę i przejście do logowania")
    def TEnterLogin(self, test_name):
        url = self.get_test_data(test_name)['url']
        self.driver.get(url)
        login_button = self.driver.find_element(By.XPATH, "//a[text()='Logowanie']")
        login_button.click()
        login_header = self.driver.find_element(By.XPATH, "//div[@class='card-header'and text()='Logowanie']")
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert login_header.text == 'Logowanie', "Brak formularza z nagłówkiem Logowanie"
