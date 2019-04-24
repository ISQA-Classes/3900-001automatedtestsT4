import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        id_name = "Raissa Amadou"
        id_address = "1110 S 67th street"
        id_state = "NE"
        id_city = "Omaha"
        id_zipcode = "68106"
        id_email = "ramadou@unomaha.edu"
        id_phone = "4022134212"
        id_username = "groyce1"
        id_password = "instructor1a"
        id_password2 = "instructor1a"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://cvong1001.pythonanywhere.com/OrganizationRegistration")
        elem = driver.find_element_by_id("id_name")
        elem.send_keys(id_name)
        elem = driver.find_element_by_id("id_address")
        elem.send_keys(id_address)
        elem = driver.find_element_by_id("id_state").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_state")
        elem.send_keys(id_state)
        elem = driver.find_element_by_id("id_city").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_city")
        elem.send_keys(id_city)
        elem = driver.find_element_by_id("id_zipcode").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys(id_zipcode)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(id_email)
        elem = driver.find_element_by_id("id_phone").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_phone")
        elem.send_keys(id_phone)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(id_username)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(id_password)
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys(id_password2)
        elem.send_keys(Keys.RETURN)
        time.sleep(100)

        elem = driver.find_element_by_class_name("save btn btn-default").click()
        time.sleep(5)
        assert "Completed Sign Up"
        #driver.get("http://127.0.0.1:8000")
        time.sleep(10)
        #driver.get("http://127.0.0.1:8000")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()




