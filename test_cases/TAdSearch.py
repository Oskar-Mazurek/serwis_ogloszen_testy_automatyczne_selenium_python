import allure
from Template import Template
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


class TAdSearch1(Template):
    @allure.step("1. Wejście na stronę i odnalezienie pola do wyszukiwania")
    def TAdSearch1(self, test_name):
        url = self.get_test_data(test_name)['url']
        self.driver.get(url)
        try:
            search_input = self.driver.find_element(By.XPATH, "//*[@placeholder = 'Wyszukaj ogłoszenie']")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            assert False, "Pole do wyszukiwania niedostępne"
