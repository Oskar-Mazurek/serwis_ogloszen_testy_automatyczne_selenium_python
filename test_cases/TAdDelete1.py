import allure
from Template import Template
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


class TAdDelete1(Template):
    @allure.step("1. Gdy użytkownik zalogowany przejście do jego profilu i odnalezienie ogłoszenia")
    def TAdDelete1(self, test_name):
        ad_name = self.get_test_data(test_name)['adName']
        try:
            profil_button = self.driver.find_element(By.XPATH, "//*[text()='Profil']")
            profil_button.click()
            ad_selector = f"//*/*[contains(text(), '{ad_name}')]"
            ad = self.driver.find_element(By.XPATH, ad_selector)
            assert ad.text == ad_name
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            return ad_selector
        except:
            assert False, "Ogłoszenie do usunięcia niedostępne"
