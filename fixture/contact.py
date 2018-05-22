from model.contact import Contact
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
        self.contact_cache = None

    def fill_contact_form(self, contact): # Contact(f_name="Edited name", l_name="Hui")
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
        self.contact_cache = None

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
        self.contact_cache = None

    def open_address_book(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("contacts") and len(wd.find_elements_by_id("panel-contact-news")) > 0):
            wd.find_element_by_xpath("//ul[@class='main-nav']//a[.='Address Book']").click()

    def count(self):
        wd = self.app.wd
        wd.get("https://www.postable.com/")
        self.open_address_book()
        return len(wd.find_elements_by_css_selector(".toggle-panel"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            wd.get("https://www.postable.com/")
            self.open_address_book()
            self.contact_cache = []
            nu = 1
            for element in wd.find_elements_by_css_selector(".toggle-panel"):
                text = element.text
                id = element.find_element_by_xpath("//ul[@id='address-book-list']/li" + "[" + str(nu) + "]").get_attribute('data-contact_id')
                self.contact_cache.append(Contact(full_name=text, id=id))
                nu += 1
        return self.contact_cache
