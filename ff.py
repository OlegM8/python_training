# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class ff(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_ff(self):
        success = True
        wd = self.wd
        wd.get("https://www.postable.com/login")
        wd.find_element_by_id("InputEmail1").click()
        wd.find_element_by_id("InputEmail1").clear()
        wd.find_element_by_id("InputEmail1").send_keys("eltrabajo@mail.ru")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("password123")
        wd.find_element_by_name("action").click()
        wd.find_element_by_xpath("//ul[@class='main-nav']//a[.='Address Book']").click()
        wd.find_element_by_css_selector("button.button").click()
        wd.find_element_by_link_text("Add a new contact").click()
        wd.find_element_by_name("contact[firstname]").click()
        wd.find_element_by_name("contact[firstname]").clear()
        wd.find_element_by_name("contact[firstname]").send_keys("ffff")
        wd.find_element_by_css_selector("button.button-panel.button-save-contact ").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
