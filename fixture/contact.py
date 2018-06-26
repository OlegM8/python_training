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
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_address_book()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='contact-info']/button[3]").click()
        wd.find_element_by_link_text("Yes, delete it!").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        self.open_address_book()
        wd.find_element_by_xpath("//ul[@id='address-book-list']/li[1]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_address_book()
        wd.find_elements_by_xpath("//ul[@id='address-book-list']/li")[index].click()

    def edit_first(self):
        self.edit_by_index(0)

    def edit_by_index(self, index, edited_contact_data):
        wd = self.app.wd
        self.open_address_book()
        self.select_contact_by_index(index)
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
                text = element.find_element_by_xpath("//ul[@id='address-book-list']/li").get_attribute('data-keywords')
                id = element.find_element_by_xpath("//ul[@id='address-book-list']/li" + "[" + str(nu) + "]")\
                    .get_attribute('data-contact_id')
                all_info = text.split()
                self.contact_cache.append(Contact(info=text, id=id,
                                                  f_name=all_info[0], l_name=all_info[1], company=all_info[2]))
                nu += 1
        return self.contact_cache

    def open_edit_contact(self, index):
        wd = self.app.wd
        self.open_address_book()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='contact-info']/button[2]").click()

    def get_info_from_edit(self, index):
        wd = self.app.wd
        self.open_edit_contact(index)
        first_name = wd.find_element_by_name("contact[firstname]").get_attribute("value")
        last_name = wd.find_element_by_name("contact[lastname]").get_attribute("value")
        company = wd.find_element_by_name("contact[company]").get_attribute("value")
        phone = wd.find_element_by_name("contact[phone]").get_attribute("value")
        id = wd.find_element_by_xpath("//ul[@id='address-book-list']/li" + "[" + str(index+1) + "]")\
            .get_attribute('data-contact_id')
        info = first_name + " " + last_name + " " + company + "  "
        return Contact(f_name=first_name, l_name=last_name, company=company, info=info, id=id, phone=phone)

    def get_info_from_select(self, index):
        wd = self.app.wd
        wd.get("https://www.postable.com/")
        self.open_address_book()
        self.contact_cache = []
        text = wd.find_element_by_xpath\
            ("//ul[@id='address-book-list']/li" + "[" + str(index+1) + "]").get_attribute('data-keywords')
        id = wd.find_element_by_xpath\
            ("//ul[@id='address-book-list']/li" + "[" + str(index+1) + "]").get_attribute('data-contact_id')
        all_info = text.split()
        self.select_contact_by_index(index)
        phone = wd.find_element_by_xpath("//div[@id='contact-info']/ul/li[1]/span").text
        return Contact(info=text, id=id, f_name=all_info[0], l_name=all_info[1],company=all_info[2],
                       phone=phone)
