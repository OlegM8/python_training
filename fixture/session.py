
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_calculator(self):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_xpath("//a").click()

    def open_homepage(self):
        wd = self.app.wd
        wd.get("https://olegtesttr.000webhostapp.com/")