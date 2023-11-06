import allure
from Template import Template
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


class TAdAddition(Template):
    @allure.step("1. Gdy użytkownik zalogowany przejście do jego profilu i kliknięcie przycisku 'Dodaj nowe ogłoszenie'")
    def TAdAddition(self, test_name):
        url = self.get_test_data(test_name)['url']
        self.driver.get(url)
        try:
            profil_button = self.driver.find_element(By.XPATH, "//*[text()='Profil']")
            profil_button.click()
            newAdButton = self.driver.find_element(By.XPATH, "//*[contains(text(),'Dodaj nowe')]")
            newAdButton.click()
            adFormTitle = self.driver.find_element(By.XPATH, "(//*[text()='Dodanie nowego ogłoszenia'])[2]")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            assert False, "formularz dodawania ogłoszenia nie wyświetlony"
