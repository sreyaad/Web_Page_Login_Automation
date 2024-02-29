import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPageAutomation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("URL_OF_YOUR_LOGIN_PAGE")

    def test_successful_login(self):
        username = "your_valid_username"
        password = "your_valid_password"

        # Locate username and password fields and login button
        username_field = self.driver.find_element(By.ID, "your_username_field_id")
        password_field = self.driver.find_element(By.ID, "your_password_field_id")
        login_button = self.driver.find_element(By.ID, "your_login_button_id")

        # Input valid credentials
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click the login button
        login_button.click()

        # Wait for the login to complete and check for successful login (you need to modify the condition based on your application)
        try:
            element_present = WebDriverWait(self.driver, 10).until(
                EC.url_contains("dashboard")  # Modify this condition based on your application
            )
            self.assertTrue(element_present, "Successful login")
        except Exception as e:
            self.fail("Login failed. Exception: {}".format(str(e)))

    def test_invalid_login(self):
        username = "your_invalid_username"
        password = "your_invalid_password"

        # Locate username and password fields and login button
        username_field = self.driver.find_element(By.ID, "your_username_field_id")
        password_field = self.driver.find_element(By.ID, "your_password_field_id")
        login_button = self.driver.find_element(By.ID, "your_login_button_id")

        # Input invalid credentials
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click the login button
        login_button.click()

        # Wait for the error message to be displayed (you need to modify the condition based on your application)
        try:
            element_present = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "your_error_message_id"))  # Modify this condition based on your application
            )
            self.assertTrue(element_present, "Invalid login error message displayed")
        except Exception as e:
            self.fail("Invalid login test failed. Exception: {}".format(str(e)))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
