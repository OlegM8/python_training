

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        self.open_address_book()
        # add new contact
        wd.find_element_by_css_selector("button.button").click()
        wd.find_element_by_link_text("Add a new contact").click()
        # fill the form
        self.fill_contact_form(contact)
        # save new contact
        wd.find_element_by_css_selector("button.button-panel.button-save-contact ").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field("contact[firstname]", contact.f_name)
        self.change_field("contact[lastname]", contact.l_name)
        self.change_field("contact[company]", contact.company)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        wd = self.app.wd
        self.open_address_book()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='contact-info']/button[3]").click()
        wd.find_element_by_link_text("Yes, delete it!").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//ul[@id='address-book-list']/li[1]").click()

    def edit_first(self, edited_contact_data):
        wd = self.app.wd
        self.open_address_book()
        self.select_first_contact()
        # open edit form
        wd.find_element_by_xpath("//div[@id='contact-info']/button[2]").click()
        # enter new values
        self.fill_contact_form(edited_contact_data)
        # submit edit
        wd.find_element_by_xpath("//div[@id='panel-contact-edit']/div/button[1]").click()

    def open_address_book(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//ul[@class='main-nav']//a[.='Address Book']").click()