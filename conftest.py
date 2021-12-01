import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                 help="Choose your language (e.g. es, fr, etc.)")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nstart browser for test..")
    driver = webdriver.Chrome(options=options)
    yield driver

    print("\nquit browser..")
    driver.quit()
