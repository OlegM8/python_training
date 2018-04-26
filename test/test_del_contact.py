

def test_delete_first_contact(app):
    app.session.login(email="eltrabajo@mail.ru", password="password123")
    app.contact.delete_first()
    app.session.logout()