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
        driver.get("https://blai.pythonanywhere.com/")
        elem = driver.find_element_by_xpath("//ul[2]/li[2]/a").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("// div / div / div / form / button").click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("cvong@unomaha.edu")
        time.sleep(3)
        elem = driver.find_element_by_xpath("// div / div / div / form / input[2]").click()
        time.sleep(3)

        assert "Email Sent"
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

