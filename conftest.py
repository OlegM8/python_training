import pytest
from fixture.application import Application


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    fixture.session.login(email="eltrabajo@mail.ru", password="password123")
    request.addfinalizer(fixture.destroy)
    return fixture
