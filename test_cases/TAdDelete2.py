import allure
from Template import Template
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


class TAdDelete2(Template):
    @allure.step("2. Kliknięcie przycisku 'Usuń' i wyświetlenie potwierdzenia usunięcia ogłoszenia")
    def TAdDelete2(self, test_name, ad_selector):
        try:
            ad_name = self.get_test_data(test_name)['adName']
            partial_delete_button_selector = "//*[contains(text(), 'Usu')]"
            full_delete_button_selector = ad_selector+"/parent::*" + partial_delete_button_selector
            ad_delete_button = self.driver.find_element(By.XPATH, full_delete_button_selector)
            ad_delete_button.click()
            delete_prompt_selector = f"//*[contains(text(),'{ad_name}')]/parent::*"
            delete_prompt = self.driver.find_element(By.XPATH, delete_prompt_selector)
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            assert 'Czy na pewno chcesz usunąć ogłoszenie o tytule:' in delete_prompt.text
            return delete_prompt_selector
        except:
            assert False, "Potwierdzenie usunięcia ogłoszenia niewidoczne"

