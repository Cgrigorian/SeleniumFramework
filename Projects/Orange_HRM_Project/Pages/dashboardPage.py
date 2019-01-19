from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    _welcome_button = """//*[@id="welcome"]"""
    _logout_button = """//*[contains(text(),'Logout')]"""
    _quick_launch_tab = """//legend[contains(text(), 'Quick Launch')]"""
    _assign_leave_button = """//*[@id="menu_leave_assignLeave"]"""

    # Dashboard page
    def at_dashboard_page(self):
        try:
            self.driver.find_element(By.XPATH, self._quick_launch_tab).is_displayed()
            print("PASS: Found dashboard page")
        except NoSuchElementException:
            print("FAIL: Dashboard page not found")

    def click_welcome(self):
        try:
            if not self.driver.find_element(By.XPATH, self._welcome_button).click():
                print("PASS: Clicked welcome button")
        except NoSuchElementException:
            print("FAIL: Unable to click welcome button")

    def click_logout(self):
        try:
            if not self.driver.find_element(By.XPATH, self._logout_button).click():
                print("PASS: Clicked logout button")
        except NoSuchElementException:
            print("FAIL: Unable to click logout button")
