
import pytest
from pages.login_page import LoginPage
from testdata import LoginTestData


@pytest.mark.usefixtures("driver")
class TestLogIn:
    @pytest.mark.parametrize("user_name", [LoginTestData.VALID_USERNAME_HR, LoginTestData.INVALID_USERNAME_HR])
    def test_login_successfully(self, driver, user_name):
        login_page = LoginPage(driver)
        login_page.log_in(user_name, LoginTestData.VALID_PASSWORD)
        assert login_page.is_user_logged_in(), "logged is not successful"
    """ 
    def test_login_fails(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in(LoginTestData.INVALID_USERNAME_HR, LoginTestData.INVALID_PASSWORD)
        assert not login_page.is_user_logged_in(), "succeed to login even credentials is wrong"
    """
