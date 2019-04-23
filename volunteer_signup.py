import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class OrganizerSignupATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_volunteer_register(self):
        id_username = "vearth"
        id_first_name = "Volunteer"
        id_last_name = "Earth"
        id_email = "vearth@unomaha.edu"
        id_password = "instructor1a"
        id_password2 = "instructor1a"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/register")
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys(id_first_name)
        time.sleep(3)
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys(id_last_name)
        time.sleep(3)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(id_email)
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(id_username)
        time.sleep(3)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(id_password)
        time.sleep(3)
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys(id_password2)
        time.sleep(10)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
