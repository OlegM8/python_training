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

class fitdog2(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_fitdog2(self):
        success = True
        wd = self.wd
        wd.get("https://stage.app.fitdogsportsclub.com/employee")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("admin@distillery.com")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("OTk3ZjE1NzUwZTIwODE4ZjlhNWZmYzI3")
        wd.find_element_by_css_selector("button.signin__submit-button.signin__submit-button_employee").click()
        wd.find_element_by_partial_link_text("Daily notes").click()
        wd.find_element_by_name("notes").send_keys("test yoyo")
        wd.find_element_by_class_name("notes-incidents__submit-button").click()
        wd.find_element_by_css_selector("button.icon-button.page-header__button").click()
        wd.find_element_by_css_selector("button.dropdown__item").click()
        ActionChains(wd).double_click(wd.find_element_by_name("email")).perform()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
