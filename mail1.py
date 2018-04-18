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

class mail1(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_mail1(self):
        success = True
        wd = self.wd
        wd.get("https://mail.ru/?from=logout")
        wd.find_element_by_id("mailbox:login").click()
        wd.find_element_by_id("mailbox:login").clear()
        wd.find_element_by_id("mailbox:login").send_keys("olegsupertest")
        wd.find_element_by_id("mailbox:password").click()
        wd.find_element_by_id("mailbox:password").clear()
        wd.find_element_by_id("mailbox:password").send_keys("kessbae17")
        wd.find_element_by_css_selector("input.o-control").click()
        wd.find_element_by_link_text("Написать письмо").click()
        wd.find_element_by_xpath("//div[@class='compose-head']/div[3]/div[1]/div/div/div[2]/div/div/div").click()
        wd.find_element_by_css_selector("textarea.js-input.compose__labels__input").click()
        wd.find_element_by_css_selector("textarea.js-input.compose__labels__input").clear()
        wd.find_element_by_css_selector("textarea.js-input.compose__labels__input").send_keys("o")
        wd.find_element_by_css_selector("div.b-correspondent__text").click()
        wd.find_element_by_name("Subject").click()
        wd.find_element_by_name("Subject").clear()
        wd.find_element_by_name("Subject").send_keys("yoyo")
        wd.find_element_by_xpath("//div[@id='b-toolbar__right']//span[.='Отправить']").click()
        wd.find_element_by_xpath("//div[@class='is-compose-empty_in']//button[.='Продолжить']").click()
        wd.find_element_by_id("PH_logoutLink").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
