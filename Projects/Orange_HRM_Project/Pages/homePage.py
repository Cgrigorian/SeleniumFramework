from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    _welcome_link = """//*[@id="welcome"]"""
    _logout_link = """//*[contains(text(),'Logout')]"""
    _dashboard_page = """//h1[contains(text(), 'Dashboard')]"""
    _assign_leave_tab_link = """//*[@id="menu_leave_assignLeave"]"""
    _dashboard_tab_link = """//*[@id="menu_dashboard_index"][contains(@href,'/index.php/dashboard')]"""

    # Dashboard page
    def at_dashboard_page(self):
        self.driver.find_element(By.XPATH, self._dashboard_page)

    # Leave page
    # TODO: create function to go to leave page
    def click_dashboard_page(self):
        self.driver.find_element(By.XPATH, self._dashboard_tab_link).click()

    def click_welcome(self):
        self.driver.find_element(By.XPATH, self._welcome_link).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self._logout_link).click()
