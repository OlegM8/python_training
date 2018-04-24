

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        self.app.open_account_page()
        wd.find_element_by_css_selector("a.text-bold").click()

    def login(self, email, password):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_xpath("//ul[@class='main-nav']//a[.='Login']").click()
        wd.find_element_by_id("InputEmail1").click()
        wd.find_element_by_id("InputEmail1").clear()
        wd.find_element_by_id("InputEmail1").send_keys(email)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("action").click()