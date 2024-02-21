from pages.base import BasePage
from locators import HomePageLocators

class HomePage(BasePage):
    def log_out(self):

        try:
            self.wait_for_clickable(HomePageLocators.log_out_link_locator).click()
        except Exception as e:
            print(f"Exception occurred while logging out: {e}")

    def navigate_to(self, navigate_to_locator):
        if navigate_to_locator == 'probevaluationpage':
            self.wait_for(HomePageLocators.probevaluation).click()
        elif navigate_to_locator == 'newEvaluation':
            self.wait_for(HomePageLocators.newEvaluation).click()
        elif navigate_to_locator == 'Home':
            try:
                self.wait_for_clickable(HomePageLocators.home_page).click()
            except Exception as e:
                print(f"Exception occurred while navigating to Home page: {e}")

