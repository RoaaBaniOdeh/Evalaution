import pytest
import  time
from testdata import LoginTestData, probEvaluationData
from pages.prob_evaluation import Evaluation
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("driver")
class TestEvaluation:

    def test_create_evaluation(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in(LoginTestData.VALID_USERNAME_HR, LoginTestData.VALID_PASSWORD)
        assert login_page.is_user_logged_in(), "logged is not successful"

        home_page = HomePage(driver)
        home_page.navigate_to('probevaluationpage')
        home_page.navigate_to('newEvaluation')

        prob_eva = Evaluation(driver)
        prob_eva.choose_employee_and_create_evaluation(probEvaluationData.EMPLOYEE_NAME)
        home_page.navigate_to('probevaluationpage')
        assert prob_eva.check_evaluation_status(probEvaluationData.CREATED_STATUS, probEvaluationData.EMPLOYEE_NAME), "Either 'Created' or 'test employee' is not present in the first row.,creat evaluation test"

    @pytest.mark.parametrize("fully_filled", [True, False])
    def test_supervisor_fill_fully_draft(self, driver,fully_filled):
        # Perform login
        login_page = LoginPage(driver)
        login_page.log_in(LoginTestData.VALID_USERNAME_SUPERVISOR, LoginTestData.VALID_PASSWORD)
        assert login_page.is_user_logged_in(), "logged is not successful"

        home_page = HomePage(driver)
        home_page.navigate_to('probevaluationpage')

        prob_eva = Evaluation(driver)
        prob_eva.view_evaluation(probEvaluationData.EMPLOYEE_NAME, probEvaluationData.CREATED_STATUS)

        prob_eva.fill_evaluation_form(probEvaluationData.ANSWER1, probEvaluationData.ANSWER2, probEvaluationData.ANSWER3,fully_filled)
        submission_status = prob_eva.submit_draft_confirm_button('Draft')
        if submission_status:
            submission_status = fully_filled
        assert submission_status == fully_filled, "Form submission status does not match expected fully_filled value,draft"

    @pytest.mark.parametrize("fully_filled", [True, False])
    def test_to_submit_not_fully_filled(self, driver,fully_filled):
        login_page = LoginPage(driver)
        login_page.log_in(LoginTestData.VALID_USERNAME_SUPERVISOR, LoginTestData.VALID_PASSWORD)
        assert login_page.is_user_logged_in(), "logged is not successful"

        home_page = HomePage(driver)
        home_page.navigate_to('probevaluationpage')

        prob_eva = Evaluation(driver)
        prob_eva.view_evaluation(probEvaluationData.EMPLOYEE_NAME, probEvaluationData.CREATED_STATUS)
        prob_eva.fill_evaluation_form(probEvaluationData.ANSWER1, probEvaluationData.ANSWER2, probEvaluationData.ANSWER3, fully_filled)

        submission_status = prob_eva.submit_draft_confirm_button('Submit')
        if submission_status:
            submission_status = fully_filled
        assert submission_status == fully_filled, "Form submission status does not match expected fully_filled value,submit"
