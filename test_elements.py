import pytest


@pytest.mark.usefixtures("login_on_admin_page")
@pytest.mark.test_login
def test_click_all_elements_on_admin_page(driver):
    driver.implicitly_wait(15)
    els = [el.text for el in driver.find_elements_by_class_name("name")]
    for el in els:
        driver.find_element_by_link_text(el).click()
        assert driver.find_element_by_tag_name('h1')
        if len(driver.find_elements_by_xpath(".//li/ul//a")) > 0:
            sub_els = [sub_els.text for sub_els in driver.find_elements_by_xpath(".//li/ul//a")]
            for sub_el in sub_els:
                driver.find_element_by_link_text(sub_el).click()
                assert driver.find_element_by_tag_name('h1')
