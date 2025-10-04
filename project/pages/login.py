from selenium.webdriver.common.by import By

class enter_password:
    def __init__(self, driver):
        self.driver = driver

    def logintest(object):
        def __init__(self, driver):
            self.driver = driver
        
        def open_website(self, url):
            self.driver.get(url)
        def login(self):
            email_input = self.driver.find_element(By.ID, user_email_object)
            email_input.click()
            email_input.clear()
            # Write email
            email_input.send_keys(user_email_object)
            # Click next