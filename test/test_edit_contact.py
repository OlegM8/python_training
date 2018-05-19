from model.contact import Contact


def test_edit_first_contact_f_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(f_name="test3"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.edit_first(Contact(f_name="Edited name", l_name="Hui"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_first_contact_company(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(f_name="teste"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.edit_first(Contact(company="Edited company"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
