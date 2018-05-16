from model.contact import Contact


def test_edit_first_contact_f_name(app):
    app.contact.edit_first(Contact(f_name="Edited name", l_name="Hui"))


def test_edit_first_contact_company(app):
    app.contact.edit_first(Contact(company="Edited company"))
