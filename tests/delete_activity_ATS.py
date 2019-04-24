import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EditActivity_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def delete_activity(self):
       user = "opendoormission"
       pwd = "test"

       driver = self.driver
       driver.maximize_window()
       driver.get("https://cvong1001.pythonanywhere.com/login")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("https://cvong1001.pythonanywhere.com")
       assert "Logged In"
       time.sleep(2)

       #path to view activity list
       driver.get("https://cvong1001.pythonanywhere.com/activity_list")

       time.sleep(1)

       # delete activity
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[7]/a").click()
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(2)

       assert "Activity Deleted"

       driver.get("https://cvong1001.pythonanywhere.com/activity_list")
       time.sleep(3)

       def tearDown(self):
           self.driver.close()


if __name__ == "__main__":
   unittest.main()
