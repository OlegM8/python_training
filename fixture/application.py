from selenium import webdriver
from fixture.session import SessionHelper
from fixture.calculator import CalcHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.calculator = CalcHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get("https://olegtesttr.000webhostapp.com/")

    def destroy(self):
        self.wd.quit()