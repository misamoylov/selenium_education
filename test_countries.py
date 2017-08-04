import pytest
import time


@pytest.mark.usefixtures("login_on_admin_page")
@pytest.mark.test_countries
def test_countries(driver):
    driver.implicitly_wait(30)
    time.sleep(5)
    driver.find_element_by_link_text("Countries").click()
    time.sleep(5)
    countries = [row.text.split()[2] for row in driver.find_elements_by_css_selector(".row")]
    assert countries == countries.sort()
