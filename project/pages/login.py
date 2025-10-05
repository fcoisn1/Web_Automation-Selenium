from selenium.webdriver.common.by import By
from utils.config import url, user, user_email_object, user_password_object, password, submitBtn

class logintest(object):
    def __init__(self, driver):
        self.driver = driver
    
    def open_web(self):
        driver = self.driver
        driver.get(url)
        # Click on user field
        user_field = driver.find_element(By.ID, user_email_object)
        user_field.clear()
        user_field.send_keys(user)
        # Click on password field
        user_field = driver.find_element(By.ID, user_password_object)
        user_field.clear()
        user_field.send_keys(password)
        # Click on continue button
        continue_button = driver.find_element(By.NAME, submitBtn)
        continue_button.click()