from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_account_page(self):
        wd = self.wd
        wd.find_element_by_link_text("Account").click()

    def add_new_contact(self, contact):
        wd = self.wd
        self.open_address_book()
        # add new contact
        wd.find_element_by_css_selector("button.button").click()
        wd.find_element_by_link_text("Add a new contact").click()
        # fill in name and company
        wd.find_element_by_name("contact[firstname]").click()
        wd.find_element_by_name("contact[firstname]").clear()
        wd.find_element_by_name("contact[firstname]").send_keys(contact.f_name)
        wd.find_element_by_name("contact[lastname]").click()
        wd.find_element_by_name("contact[lastname]").clear()
        wd.find_element_by_name("contact[lastname]").send_keys(contact.l_name)
        wd.find_element_by_name("contact[company]").click()
        wd.find_element_by_name("contact[company]").clear()
        wd.find_element_by_name("contact[company]").send_keys(contact.company)
        # save new contact
        wd.find_element_by_css_selector("button.button-panel.button-save-contact ").click()

    def open_address_book(self):
        wd = self.wd
        wd.find_element_by_xpath("//ul[@class='main-nav']//a[.='Address Book']").click()

    def open_homepage(self):
        wd = self.wd
        wd.get("https://www.postable.com/")

    def destroy(self):
        self.wd.quit()