import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class AddProfileAdminATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"

        # Create profile in admin page
        driver = self.driver
        driver.maximize_window()
        driver.get("http://cvong1001.pythonanywhere.com/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.get("http://cvong1001.pythonanywhere.com/admin/volunnet/profile/add/")
        select = Select(driver.find_element_by_id("id_user"))
        time.sleep(2)
        select.select_by_value("2")
        time.sleep(2)
        elem = driver.find_element_by_name("_save").click()

        # Show in pythonanywhere
        driver.get("http://cvong1001.pythonanywhere.com/")
        time.sleep(2)
        driver.get("http://cvong1001.pythonanywhere.com//profile")



        assert "Profile Created"
        time.sleep(3)

        def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    unittest.main()
