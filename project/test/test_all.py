from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import unittest
from pages.login import logintest
from utils.config import chromedriver
import time


class TestAll(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        s = Service(chromedriver)
        cls.driver = webdriver.Chrome(service=s)
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(120)

    def testcase(self):
        login = logintest(self.driver)
        login.open_web()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()