from model.calculator import Calculator


class CalcHelper:

    def __init__(self, app):
        self.app = app

    def addition(self):
        wd = self.app.wd
        self.open_calculator()
        self.fill()

    def open_calculator(self):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_xpath("//a").click()

    def fill(self, f, s):
        wd = self.app.wd
        wd.find_element_by_id("f").send_keys(f)
        wd.find_element_by_id("s").send_keys(s)

    def click_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@type='button']").click()

    def select_operator(self, o):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@id='sym']//option["+str(o)+"]").click()

    def text_result(self):
        wd = self.app.wd
        return wd.find_element_by_id("res").text