

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element_by_xpath("//ul[@class='main-nav']//a[.='Address Book']").click()