# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.session.login(email="eltrabajo@mail.ru", password="password123")
    app.contact.add_new(Contact(f_name="test", l_name="test2", company="company test"))
    app.session.logout()


def test_add_new_empty_contact(app):
    app.session.login(email="eltrabajo@mail.ru", password="password123")
    app.contact.add_new(Contact(f_name="test", l_name="", company=""))
    app.session.logout()
