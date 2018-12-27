from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    _username_textbox = """//*[@id="txtUsername"]"""
    _password_textbox = """//*[@id="txtPassword"]"""
    _login_button = """//*[@id="btnLogin"]"""

    def enter_username(self, username):
        try:
            if not self.driver.find_element(By.XPATH, self._username_textbox).clear():
                print("PASS: Username textbox cleared")
        except NoSuchElementException:
            print("FAIL: Username textbox not cleared")
        try:
            if not self.driver.find_element(By.XPATH, self._username_textbox).send_keys(username):
                print("PASS: Entered username({}) in textbox".format(username))
        except NoSuchElementException:
            print("FAIL: Unable to enter username({}) in textbox".format(username))

    def enter_password(self, password):
        try:
            if not self.driver.find_element(By.XPATH, self._password_textbox).clear():
                print("PASS: Cleared the password textbox")
        except NoSuchElementException:
            print("FAIL: Password textbox not cleared")
        try:
            if not self.driver.find_element(By.XPATH, self._password_textbox).send_keys(password):
                print("PASS: Entered password:({}) in textbox".format(password))
        except NoSuchElementException:
            print("FAIL: Unable to enter password({}) in textbox".format(password))

    def click_login(self):
        try:
            if not self.driver.find_element(By.XPATH, self._login_button).click():
                print("PASS: Clicked login button")
        except NoSuchElementException:
            print("FAIL: Unable to click login button")
