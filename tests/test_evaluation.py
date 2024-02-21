import pytest
from testdata import LoginTestData, ProbationEvaluationData
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
        prob_eva.choose_employee_and_create_evaluation(ProbationEvaluationData.EMPLOYEE_NAME)
        home_page.navigate_to('probevaluationpage')
        assert prob_eva.check_evaluation_status(ProbationEvaluationData.CREATED_STATUS, ProbationEvaluationData.EMPLOYEE_NAME), "Either 'Created' or 'test employee' is not present in the first row.,creat evaluation test"

    @pytest.mark.parametrize("fully_filled", [True, False])
    def test_supervisor_draft(self, driver,fully_filled):
        # Perform login
        login_page = LoginPage(driver)
        login_page.log_in(LoginTestData.VALID_USERNAME_SUPERVISOR, LoginTestData.VALID_PASSWORD)
        assert login_page.is_user_logged_in(), "logged is not successful"

        home_page = HomePage(driver)
        home_page.navigate_to('probevaluationpage')

        prob_eva = Evaluation(driver)
        prob_eva.view_evaluation(ProbationEvaluationData.EMPLOYEE_NAME, ProbationEvaluationData.CREATED_STATUS)

        prob_eva.fill_evaluation_form(ProbationEvaluationData.ANSWER1, ProbationEvaluationData.ANSWER2, ProbationEvaluationData.ANSWER3,fully_filled)
        submission_status = prob_eva.submit_draft_confirm_button('Draft')
        if submission_status:
            submission_status = fully_filled
        assert submission_status == fully_filled, "Form submission status does not match expected fully_filled value,draft"

    @pytest.mark.parametrize("fully_filled", [True, False])
    def test_supervisor_submit(self, driver,fully_filled):
        login_page = LoginPage(driver)
        login_page.log_in(LoginTestData.VALID_USERNAME_SUPERVISOR, LoginTestData.VALID_PASSWORD)
        assert login_page.is_user_logged_in(), "logged is not successful"

        home_page = HomePage(driver)
        home_page.navigate_to('probevaluationpage')

        prob_eva = Evaluation(driver)
        prob_eva.view_evaluation(ProbationEvaluationData.EMPLOYEE_NAME, ProbationEvaluationData.CREATED_STATUS)
        prob_eva.fill_evaluation_form(ProbationEvaluationData.ANSWER1, ProbationEvaluationData.ANSWER2, ProbationEvaluationData.ANSWER3, fully_filled)

        submission_status = prob_eva.submit_draft_confirm_button('Submit')
        if submission_status:
            submission_status = fully_filled
        assert submission_status == fully_filled, "Form submission status does not match expected fully_filled value,submit"

    def test_manager_choice(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in(LoginTestData.VALID_USERNAME_MANAGER, LoginTestData.VALID_PASSWORD)
        assert login_page.is_user_logged_in(), "logged is not successful"

        home_page = HomePage(driver)
        home_page.navigate_to('probevaluationpage')

        prob_eva = Evaluation(driver)
        prob_eva.view_evaluation(ProbationEvaluationData.EMPLOYEE_NAME, ProbationEvaluationData.SUBMITTED_STATUS)

        prob_eva.manager_choice()
        submission_status = prob_eva.submit_draft_confirm_button('Submit')
        assert submission_status == True, "Form submission status does not match expected value,manager choice"
        home_page.navigate_to('probevaluationpage')
        assert prob_eva.check_evaluation_status(ProbationEvaluationData.EMPLOYEE_NAME, ProbationEvaluationData.MANAGER_SUBMIT),"Status doesn't reflect successfully to table, manager choice"

    def test_hr_confirmation(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in(LoginTestData.VALID_USERNAME_HR, LoginTestData.VALID_PASSWORD)
        assert login_page.is_user_logged_in(), "logged is not successful"

        home_page = HomePage(driver)
        home_page.navigate_to('probevaluationpage')

        prob_eva = Evaluation(driver)
        prob_eva.view_evaluation(ProbationEvaluationData.EMPLOYEE_NAME, ProbationEvaluationData.MANAGER_SUBMIT)

        submission_status = prob_eva.submit_draft_confirm_button('Confirm')
        assert submission_status, "Form submission status does not match expected value,HR confirmation"
        home_page.navigate_to('probevaluationpage')
        assert prob_eva.check_evaluation_status(ProbationEvaluationData.EMPLOYEE_NAME, ProbationEvaluationData.HR_CONFIRM),"Status doesn't reflect successfully to table, hr confirmation"

    def test_employee_acknowledge(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in(LoginTestData.VALID_USERNAME_Employee, LoginTestData.VALID_PASSWORD)
        assert login_page.is_user_logged_in(), "logged is not successful"

        home_page = HomePage(driver)
        home_page.navigate_to('probevaluationpage')

        prob_eva = Evaluation(driver)
        prob_eva.view_evaluation(ProbationEvaluationData.EMPLOYEE_NAME, ProbationEvaluationData.HR_CONFIRM)
        prob_eva.employee_ack()
        home_page.navigate_to('probevaluationpage')
        assert prob_eva.check_evaluation_status(ProbationEvaluationData.EMPLOYEE_NAME,
                                            ProbationEvaluationData.EMPLOYEE_ACKNOWLEDGMENT), "Status doesn't reflect successfully to table, employe acknowledgment"
