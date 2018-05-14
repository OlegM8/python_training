from model.contact import Contact


def test_edit_first_contact_f_name(app):
    app.session.login(email="eltrabajo@mail.ru", password="password123")
    app.contact.edit_first(Contact(f_name="Edited name", l_name="Hui"))
    app.session.logout()


def test_edit_first_contact_company(app):
    app.session.login(email="eltrabajo@mail.ru", password="password123")
    app.contact.edit_first(Contact(company="Edited company"))
    app.session.logout()