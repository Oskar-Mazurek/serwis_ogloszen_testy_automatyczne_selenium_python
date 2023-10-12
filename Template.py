from selenium import webdriver
import json


class Template():
    driver = webdriver.Chrome()
    driver.implicitly_wait(0.5)

    def get_test_data(self, test_name: str) -> dict:
        f = open('testsData.json', 'r')
        data = json.load(f)
        f.close()
        return data[test_name]
