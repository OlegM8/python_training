# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_new_contact(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new(Contact(f_name="test", l_name="test2", company="company test"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_new_empty_contact(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new(Contact(f_name="test", l_name="", company=""))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)