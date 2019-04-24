import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class VolLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "vearth"
        time.sleep(2)
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://cvong1001.pythonanywhere.com/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://cvong1001.pythonanywhere.com")
        assert "Logged In"
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()




