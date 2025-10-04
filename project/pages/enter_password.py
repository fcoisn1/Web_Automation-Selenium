from selenium.webdriver.common.by import By
from utils.config import task_menu, new_task, title, save_button, task_completed_button, task_completed_object_message, task_completed_message

class enter_password:
    def __init__(self, driver):
        self.driver = driver

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)

    def click_next(self):
        next_button = self.driver.find_element(By.ID, "next")
        next_button.click()