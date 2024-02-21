from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#password')
    USERNAME_INPUT = (By.CSS_SELECTOR, '#email')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[type=submit]')
    PERFORMANCE_EVALUATION = (By.XPATH, "//h4[contains(text(), 'Performance Evaluation')]")


class HomePageLocators:
    log_out_link_locator = (By.CSS_SELECTOR, 'a[href="/Home/LogOut"]')
    probevaluation = (By.LINK_TEXT, 'Probation Evaluation')
    newEvaluation = (By.CSS_SELECTOR, "form[action='/Probation/NewEvaluationButtonClick'][method='post']")
    home_page = (By.LINK_TEXT, 'Home')


class EvaluationLocators:
    ID_MENU_NAME = (By.ID, "name")
    CREATE_EVALUATION_BTN = (By.CLASS_NAME, "btn-primary")
    EVALUATIONS_TABLE = (By.CSS_SELECTOR, 'tbody')
    FIRST_ROW_OF_EVALUATION_TABLE = (By.CSS_SELECTOR, 'tbody tr:first-child')
    Answer4_ID = (By.ID, "answer-4")
    Answer2_ID = (By.ID, "answer-3")
    Answer1_ID = (By.ID, "answer-1")
    manageEvalTable_Selector = (By.ID, "manageEvalTable")
    manageEvalTable_Selector_row = (By.CSS_SELECTOR, "#manageEvalTable tbody tr")
    ANSWERS_SECTION = (By.CLASS_NAME, "well")

