from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(f_name="test3"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.edit_by_index(index, Contact(f_name="Edited name", l_name="Hui"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    new_contacts = sorted(new_contacts, key=Contact.id_or_max)
    assert sorted(old_contacts, key=Contact.id_or_max) != sorted(new_contacts, key=Contact.id_or_max)


def test_edit_first_contact_company(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(f_name="teste"))
    old_contacts = app.contact.get_contacts_list()
    index = 0
    app.contact.edit_by_index(index, Contact(company="Edited company"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)

