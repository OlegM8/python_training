# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from daily_notes import Daily_notes

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class fitdog2(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(20)
    
    def test_new_note(self):
        wd = self.wd
        self.open_employee_home(wd)
        self.login(wd, email="admin@distillery.com", password="OTk3ZjE1NzUwZTIwODE4ZjlhNWZmYzI3")
        self.open_daily_notes(wd)
        self.add_new_note(wd, Daily_notes(note_text="test yoyo"))
        self.logout(wd)

    def test_new_max_note(self):
        wd = self.wd
        self.open_employee_home(wd)
        self.login(wd, email="admin@distillery.com", password="OTk3ZjE1NzUwZTIwODE4ZjlhNWZmYzI3")
        self.open_daily_notes(wd)
        self.add_new_note(wd, Daily_notes(note_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsuLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsuLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsuLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsuLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsuLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsuLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsuLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor imsumt"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_css_selector("button.icon-button.page-header__button").click()
        wd.find_element_by_css_selector("button.dropdown__item").click()

    def add_new_note(self, wd, daily_notes):
        # enter note text
        wd.find_element_by_name("notes").send_keys(daily_notes.note_text)
        # add note
        wd.find_element_by_class_name("notes-incidents__submit-button").click()

    def open_daily_notes(self, wd):
        wd.find_element_by_partial_link_text("Daily notes").click()

    def login(self, wd, email, password):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("button.signin__submit-button.signin__submit-button_employee").click()

    def open_employee_home(self, wd):
        wd.get("https://stage.app.fitdogsportsclub.com/employee")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
