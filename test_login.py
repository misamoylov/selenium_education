import pytest


@pytest.mark.test_login
def test_login(driver):
    driver.get("http://localhost/public_html/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
