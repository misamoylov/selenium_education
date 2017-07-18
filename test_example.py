import pytest


@pytest.mark.usefixtures('driver')
def test_example(driver):
    driver.get("http://www.google.com/")
