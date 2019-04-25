import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class apply(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def apply(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://cvong1001.pythonanywhere.com")
        elem = driver.find_element_by_xpath(" // ul[2] / li / a").click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("blai")
        time.sleep(1)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("test")
        time.sleep(1)
        elem = driver.find_element_by_xpath("//div/div/div/form/input[2]").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("//div/div/div/div[2]/div/div/div/div/div/div/div/p[2]/a").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("//div/div/div[3]/table/tbody/tr[1]/td[7]/a").click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_title")
        time.sleep(2)
        elem.send_keys("Gathering Litter")
        time.sleep(1)

        elem = driver.find_element_by_id("id_vol_name")
        elem.send_keys("Calvin")
        time.sleep(1)

        elem = driver.find_element_by_id("id_email")
        elem.send_keys("cvong@unomaha.edu")
        time.sleep(1)

        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("1234567890")
        time.sleep(1)

        elem = driver.find_element_by_xpath("//div/div/div/form/button").click()

        time.sleep(3)

        assert "Organization Added"
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
   unittest.main()