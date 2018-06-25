from selenium import webdriver
from fixture.session import SessionHelper
from fixture.calculator import CalcHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
<<<<<<< HEAD
        self.contact = ContactHelper(self)
=======
        self.calculator = CalcHelper(self)
>>>>>>> a357c2c25e91ad19f1c2bfcb19274388fbbf7aa0


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