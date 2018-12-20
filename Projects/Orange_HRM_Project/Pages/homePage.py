from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    _welcome_link = """//*[@id="welcome"]"""
    _logout_link = """//*[contains(text(),'Logout')]"""

    def click_welcome(self):
        self.driver.find_element(By.XPATH, self._welcome_link).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self._logout_link).click()
