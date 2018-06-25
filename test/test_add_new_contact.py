# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new(Contact(f_name="test", l_name="test2", company="company test"))
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    new_contacts = sorted(new_contacts, key=Contact.id_or_max)
    old_contacts.append(new_contacts[-1])
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_new_empty_contact(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new(Contact(f_name="test", l_name="", company=""))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    new_contacts = sorted(new_contacts, key=Contact.id_or_max)
    old_contacts.append(new_contacts[-1])
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)