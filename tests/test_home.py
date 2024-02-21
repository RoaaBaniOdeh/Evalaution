import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from testdata import LoginTestData


@pytest.mark.usefixtures("driver")
class TestHome:

    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in(LoginTestData.VALID_USERNAME_HR, LoginTestData.VALID_PASSWORD)
        assert login_page.is_user_logged_in(), "logged is not successful"
        home_page = HomePage(driver)
        home_page.log_out()

    def test_navigate(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in(LoginTestData.VALID_USERNAME_HR, LoginTestData.VALID_PASSWORD)
        home_page = HomePage(driver)
        home_page.navigate_to('probevaluationpage')
        home_page.navigate_to('newEvaluation')
