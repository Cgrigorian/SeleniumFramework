from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Projects.Orange_HRM_Project.Pages.loginPage import LoginPage
from Projects.Orange_HRM_Project.Pages.homePage import HomePage


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver\
            .Firefox(executable_path="C:/Users/chris/PycharmProjects/SeleniumFramework/Drivers/geckodriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/chris/PycharmProjects/SeleniumFramework'
                                                                  '/Reports'))
