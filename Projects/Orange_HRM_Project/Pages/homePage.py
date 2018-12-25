from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    _welcome_link = """//*[@id="welcome"]"""
    _logout_link = """//*[contains(text(),'Logout')]"""
    _dashboard_quick_launch = """//legend[contains(text(), 'Quick Launch')]"""
    _assign_leave_tab_link = """//*[@id="menu_leave_assignLeave"]"""
    _dashboard_tab_link = """//*[@id="menu_dashboard_index"][contains(@href,'/index.php/dashboard')]"""

    # Dashboard page
    def at_dashboard_page(self):
        try:
            self.driver.find_element(By.XPATH, self._dashboard_quick_launch).is_displayed()
            print("PASS: Found dashboard page")
        except NoSuchElementException:
            print("FAIL: Dashboard page not found")

    # Leave page

    # Header
    def click_welcome(self):
        if not self.driver.find_element(By.XPATH, self._welcome_link).click():
            print("PASS: Clicked welcome button")
        else:
            print("FAIL: Unable to click welcome button")

    def click_logout(self):
        if not self.driver.find_element(By.XPATH, self._logout_link).click():
            print("PASS: Clicked logout button")
        else:
            print("FAIL: Unable to click logout button")
