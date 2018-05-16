# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.contact.add_new(Contact(f_name="test", l_name="test2", company="company test"))


def test_add_new_empty_contact(app):
    app.contact.add_new(Contact(f_name="test", l_name="", company=""))
