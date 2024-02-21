from selenium.webdriver.common.by import By
from pages.base import BasePage
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
# from locators import EvaluationLocators


class Evaluation(BasePage):
    ID_MENU_NAME = (By.ID, "name")
    CREATE_EVALUATION_BTN = (By.CLASS_NAME, "btn-primary")
    EVALUATIONS_TABLE = (By.CSS_SELECTOR, 'tbody')
    FIRST_ROW_OF_EVALUATION_TABLE = (By.CSS_SELECTOR, 'tbody tr:first-child')
    # emp_name = EvaluationLocators.ID_MENU_NAME
    manageEvalTable_Selector = (By.ID, "manageEvalTable")
    manageEvalTable_Selector_row = (By.CSS_SELECTOR, "#manageEvalTable tbody tr")
    ANSWERS_SECTION = (By.CLASS_NAME, "well")
    CHECK_BOXES = (By.CSS_SELECTOR, "input[type='checkbox']")
    Answer4_ID = (By.ID, "answer-4")
    Answer2_ID = (By.ID, "answer-3")
    Answer1_ID = (By.ID, "answer-1")

    '''

    ROWS_OF_TABLE = (By.CSS_SELECTOR, "tbody tr")
    VIEW_BTN = (By.CSS_SELECTOR, "button.btn-info")
    save_draft_button_locator = (By.XPATH, "//button[contains(., 'Save Draft')]")
    submit_form_button_locator = (By.XPATH, "//button[contains(., 'Submit Form')]")
    '''

    def choose_employee_and_create_evaluation(self, employee_name):
        dropdown = self.find(*self.ID_MENU_NAME)
        select = Select(dropdown)
        select.select_by_visible_text(employee_name)
        self.find(*self.CREATE_EVALUATION_BTN).click()

    def check_evaluation_status(self, evaluation_status, employee_name):
        first_row = self.wait_for(self.EVALUATIONS_TABLE).find_element(*self.FIRST_ROW_OF_EVALUATION_TABLE)
        cells = first_row.find_elements(By.TAG_NAME, 'td')
        cell_texts = [cell.text.strip() for cell in cells]
        if evaluation_status in cell_texts and employee_name in cell_texts:
            return True
        else:
            return False

    def view_evaluation(self, employee_name, evaluation_status):
        self.wait_for_visible(self.manageEvalTable_Selector)
        rows = self.wait_for_elements(self.manageEvalTable_Selector_row)
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, 'td')
            if columns[0].text.strip() == employee_name and columns[3].text.strip() == evaluation_status:
                try:
                    view_button = row.find_element(By.CSS_SELECTOR, "button.btn-info")
                    ActionChains(self.driver).move_to_element(view_button).perform()
                    view_button.click()
                    break
                except Exception as e:
                    print(f"Error clicking view button: {e}")

    def fill_evaluation_form(self, answer_1, answer_2, answer_3, fully_filled=True):
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            checkboxes = row.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
            if checkboxes:
                num_checkboxes_to_click = random.randint(1, len(checkboxes)) if fully_filled else random.randint(0,
                                                                                                                 len(checkboxes) - 1)
                choices = random.sample(range(len(checkboxes)), num_checkboxes_to_click)
                for choice in choices:
                    checkboxes[choice].click()

        section = self.wait_for_visible(self.ANSWERS_SECTION)
        textareas = [
            section.find_element(*self.Answer1_ID),
            section.find_element(*self.Answer2_ID),
            section.find_element(*self.Answer4_ID)
        ]
        textarea_indices = [0, 1, 2]
        counter = 0
        for textarea_index in textarea_indices:
            textareas[textarea_index].clear()
            if fully_filled or random.choice([True, False]):
                textareas[textarea_index].send_keys([answer_1, answer_2, answer_3][counter])
            counter += 1

    def submit_draft_confirm_button(self, choice):
        try:
            footer = self.wait_for_visible((By.CLASS_NAME, "mb-5.flex.justify-end"))
            if choice == 'Submit':
                submit_button = footer.find_element(By.XPATH, "//button[@class='btn btn-primary rounded-2']")
                submit_button.click()
                return True
            elif choice == 'Draft':
                draft_button = footer.find_element(By.XPATH, "//button[@value='draft']")
                draft_button.click()
                return True
            elif choice == 'Confirm':
                confirm_btn = self.wait_for_clickable((By.CSS_SELECTOR, "footer .btn.btn-primary"))
                confirm_btn.click()
                return True
            return False
        except TimeoutException:
            print("Timeout occurred while waiting for the footer or button to be visible.")
            return False

    def manager_choice(self):
        section_element = self.find(*(By.XPATH, "//section[h2[contains(., 'Project/ Department Head’s Decision')]]"))
        radio_buttons = section_element.find_elements(By.CSS_SELECTOR, "label.block input[type='radio']")
        if not radio_buttons:
            print("No radio buttons found within the section element.")
        else:
            random_radio_button = random.choice(radio_buttons)
            random_radio_button.click()
            print("filled.")

    def employee_ack(self):
        self.wait_for_visible((By.CSS_SELECTOR, "footer.mb-5"))
        checkbox = self.wait_for_clickable((By.ID, "ack-box"))
        checkbox.click()
        acknowledge_button = self.wait_for_clickable((By.CSS_SELECTOR, "button.btn-primary"))
        acknowledge_button.click()

