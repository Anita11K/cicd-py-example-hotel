import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
import pytest


# URL = 'http://hotel-v3.progmasters.hu/'
# options = Options()
# options.add_argument('window-position=-1300,-200')
# options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(options=options)
#
# browser.get(URL)
# browser.maximize_window()
#
# login_btn = browser.find_element(By.XPATH, '//a[@class="nav-link"]')
# login_btn.click()
#
# email_input = browser.find_element(By.ID, 'email')
# email_input.send_keys('hiwasi1765@wisnick.com')
#
# password_input = browser.find_element(By.ID, 'password')
# password_input.send_keys('tesztelek2021')
#
# submit_btn = browser.find_element(By.NAME, 'submit')
# submit_btn.click()
# time.sleep(1)
#
# logout_btn = browser.find_element(By.ID, 'logout-link')
#
# assert logout_btn.text == "Kilépés"

class TestHootel(object):
    def setup_method(self):
        URL = 'http://hotel-v3.progmasters.hu/'
        options = Options()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        self.browser.maximize_window()

    def teardown_method(self):
        self.browser.quit()

    # @pytest.mark.skip(reason='Erre most nincs szükség')
    # @pytest.mark.skipif(True, reason='Erre most nincs szükség')
    @pytest.mark.parametrize("email, password", [('', '')])
    @allure.title("Hootel Login")
    @allure.description("A belépés tesztelése")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("login")
    def test_login(self, email, password):
        login_btn = self.browser.find_element(By.XPATH, '//a[@class="nav-link"]')
        login_btn.click()

        email_input = self.browser.find_element(By.ID, 'email')
        email_input.send_keys(email)

        password_input = self.browser.find_element(By.ID, 'password')
        password_input.send_keys(password)

        submit_btn = self.browser.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(1)

        logout_btn = self.browser.find_element(By.ID, 'logout-link')

        assert logout_btn.text == "Kilépés"

    def test_hotel_list(self):
        hotel_list_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list_btn.click()
        time.sleep(1)

        hotel_list = self.browser.find_elements(By.XPATH, '//h4[@style="cursor: pointer"]')
        assert len(hotel_list) != 0
        assert len(hotel_list) == 10
