import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        baseURL = request.config.getoption("--baseURL")
        fixture = Application(browser=browser, baseURL=baseURL)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, baseURL=baseURL)
    fixture.session.ensure_login(email="eltrabajo@mail.ru", password="password123")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseURL", action="store", default="https://www.postable.com/")