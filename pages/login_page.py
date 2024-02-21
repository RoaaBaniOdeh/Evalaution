from selenium.common import NoSuchElementException
from pages.base import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):

    def log_in(self, username, userpassword):

        self.wait_for(LoginPageLocators.USERNAME_INPUT).send_keys(username)
        self.wait_for(LoginPageLocators.PASSWORD_INPUT).send_keys(userpassword)
        self.find(*LoginPageLocators.LOGIN_BTN).click()

    def is_user_logged_in(self):
        try:
            performance_evaluation_element = self.driver.find_element(*LoginPageLocators.PERFORMANCE_EVALUATION)
            return performance_evaluation_element.is_displayed() and "Performance Evaluation" in performance_evaluation_element.text
        except NoSuchElementException:
            return False

