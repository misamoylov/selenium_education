import os
import platform
import pytest

from selenium import webdriver


@pytest.fixture
def driver(request):
    if platform.system() == 'Linux':
        wd = webdriver.Firefox()
    elif platform.system() == 'Windows':
        wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Nightly\\firefox.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd
