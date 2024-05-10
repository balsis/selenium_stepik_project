import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome, firefox or safari")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: '--language=en' or '--language=ru'")


def get_options(driver_name, user_language):
    browsers = {
        "chrome": webdriver.ChromeOptions,
        "firefox": webdriver.FirefoxOptions,
        "safari": webdriver.SafariOptions
    }

    try:
        options = browsers[driver_name]()
    except KeyError:
        raise ValueError(f"Unsupported browser: {driver_name}")

    options.page_load_strategy = 'eager'
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--incognito')
    options.add_argument("--disable-cache")
    options.add_argument('--headless')
    if driver_name == "chrome":
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
    elif driver_name == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", user_language)
        options.profile = profile
    elif driver_name == "safari":
        options.add_argument(f'--lang={user_language}')
    return options


@pytest.fixture(scope="function")
def driver(request):
    driver_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")

    driver = None
    options = get_options(driver_name, user_language)

    if driver_name == "chrome":
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome(options=options)
    elif driver_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox(options=options)
    elif driver_name == "safari":
        print("\nstart safari browser for test..")
        driver = webdriver.Safari(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or safari")

    yield driver
    print("\nquit browser..")
    driver.quit()
