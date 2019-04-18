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
        driver.get("https://blai.pythonanywhere.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("instructor")
        time.sleep(1)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("instructor1a")
        time.sleep(1)
        elem = driver.find_element_by_xpath("//div[3]/input").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("// div[2] / table / tbody / tr[2] / td[1] / a").click()
        time.sleep(3)
        select = Select(driver.find_element_by_id("id_user"))
        time.sleep(2)
        select.select_by_value("2")
        time.sleep(1)

        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Fake Org")
        time.sleep(1)

        elem = driver.find_element_by_id("id_address")
        elem.send_keys("1234 Fake Address")
        time.sleep(1)

        driver.find_element_by_id("id_city").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        time.sleep(1)

        driver.find_element_by_id("id_state").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_state")
        elem.send_keys("NE")
        time.sleep(1)

        driver.find_element_by_id("id_phone").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_phone")
        elem.send_keys("4023214234")
        time.sleep(1)

        driver.find_element_by_id("id_zipcode").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("68127")
        time.sleep(1)

        elem = driver.find_element_by_id("id_email")
        elem.send_keys("cvong@unomaha.edu")
        time.sleep(1)

        assert "Organization Added"
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

