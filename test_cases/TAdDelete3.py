import allure
from Template import Template
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


class TAdDelete3(Template):
    @allure.step("2. Kliknięcie przycisku 'Potwierdź usunięcie' i wyświetlenie komiunikatu")
    def TAdDelete3(self, test_name, delete_prompt_selector):
        try:
            ad_name = self.get_test_data(test_name)['adName']
            delete_prompt_selector += "/parent::*"
            delete_submit_button_selector = delete_prompt_selector+"//*[contains(text(),'Potwierdź usunięcie')]"
            delete_submit_button = self.driver.find_element(By.XPATH, delete_submit_button_selector)
            delete_submit_button.click()
            success_info = self.driver.find_element(By.XPATH, "//div[@role = 'alert']")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            assert success_info.text == "Usunięto ogłoszenie!", "Nie udało się usunąć ogłoszenia"
        except:
            assert False, "Nie udało się usunąć ogłoszenia"
