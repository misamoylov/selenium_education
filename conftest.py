import os
import platform
import pytest

from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    if platform.system() == 'Linux':
        wd = webdriver.Firefox()
    elif platform.system() == 'Windows':
        wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Nightly\\firefox.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


@pytest.mark.usefixtures("driver")
@pytest.fixture(scope="function")
def login_on_admin_page(driver):
    driver.get("http://localhost/public_html/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
