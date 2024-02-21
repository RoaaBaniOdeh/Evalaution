from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def find_s(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))


