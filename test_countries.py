import pytest
import time


# @pytest.mark.usefixtures("login_on_admin_page")
# @pytest.mark.test_countries
# def test_countries(driver):
#     driver.implicitly_wait(30)
#     time.sleep(5)
#     driver.find_element_by_link_text("Countries").click()
#     time.sleep(5)
#     countries = [row.text.split()[2] for row in driver.find_elements_by_css_selector(".row")]
#
#     assert countries == countries.sort()


@pytest.mark.usefixtures("login_on_admin_page")
@pytest.mark.test_geo_zones
def test_geo_zones(driver):
    driver.implicitly_wait(30)
    driver.get("http://localhost/public_html/admin/?app=geo_zones&doc=geo_zones")
    countries = [row.text for row in driver.find_elements_by_css_selector(".row>td:nth-of-type(3)>a")]
    for country in countries:
        driver.find_element_by_link_text(country).click()
        zones = [zone.text for zone in driver.find_elements_by_css_selector("select[name $=\"[zone_code]\"]"
                                                                            " option[selected = \"selected\"]")]
        assert zones == zones.sort()
        driver.get("http://localhost/public_html/admin/?app=geo_zones&doc=geo_zones")
