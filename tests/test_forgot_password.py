import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class forgotPassword(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://cvong1001.pythonanywhere.com/login")
        time.sleep(2)
        driver.get("http://cvong1001.pythonanywhere.com/password_reset/")
        elem = driver.find_element_by_id("id_email")
        time.sleep(3)
        elem.send_keys("cvong@unomaha.edu")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[3]").click()
        time.sleep(3)

        assert "Email Sent"
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

