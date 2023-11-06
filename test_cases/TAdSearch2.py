import allure
from Template import Template
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

class TAdSearch2(Template):
    @allure.step("2. Wpisanie nazwy samochodu do pola wyszukiwania, kliknięcie przycisku 'Wyszukaj'")
    def TAdSearch2(self, test_name):
        search_data = self.get_test_data(test_name)['search_data']
        try:
            search_input = self.driver.find_element(By.XPATH, "//*[@placeholder = 'Wyszukaj ogłoszenie']")
            search_input.send_keys(search_data['car_name'])
            search_button = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Wyszukaj')]")
            search_button.click()
        except:
            assert False, "Błąd w wyszukiwaniu poszukiwanego samochodu"
        try:
            searched_car = self.driver.find_element(By.XPATH,
                                                    f"(//*[contains(text(), '{search_data['car_name']}')])[2]")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

        except:
            assert False, "Nie znaleziono poszukiwanego samochodu"
