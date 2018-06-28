# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.contacts import constant as testdata


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    new_contacts = sorted(new_contacts, key=Contact.id_or_max)
    old_contacts.append(new_contacts[-1])
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)