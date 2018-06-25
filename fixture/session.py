

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        self.open_account_page()
        wd.implicitly_wait(10)
        wd.find_element_by_link_text("Account").click()
        wd.find_element_by_xpath("//a[@class='text-bold']").click()

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

    def open_account_page(self):
        wd = self.app.wd
        wd.find_element_by_class_name("nav-account ").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Account")) > 0

    def is_logged_in_as(self, email):
        wd = self.app.wd
        wd.get("https://www.postable.com/account/")
        return wd.find_element_by_class_name("request-email").text == email

    def ensure_login(self, email, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(email):
                return
            else:
                self.logout()
        self.login(email, password)
