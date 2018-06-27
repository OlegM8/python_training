from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, baseURL):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.baseURL = baseURL


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get(self.baseURL)

    def destroy(self):
        self.wd.quit()