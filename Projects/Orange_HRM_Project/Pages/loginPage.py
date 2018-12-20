from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    _username_textbox = """//*[@id="txtUsername"]"""
    _password_textbox = """//*[@id="txtPassword"]"""
    _login_button = """//*[@id="btnLogin"]"""

    def enter_username(self, username):
        # self.driver.find_element(By.ID, self._username_textbox).clear()
        self.driver.find_element(By.XPATH, self._username_textbox).clear()
        self.driver.find_element(By.XPATH, self._username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self._password_textbox).clear()
        self.driver.find_element(By.XPATH, self._password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self._login_button).click()
