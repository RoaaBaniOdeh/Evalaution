# TestAutomation-EvaluationProbation
This is a test automation for the Probation Evaluation System at Asal Technology Company to evaluate employees during their 3-6 month trial period.

## Language : 
  python
  
## Built With 
 * [Pytest](https://docs.pytest.org/en/latest/getting-started.html) - Core test framework
 * [Selenium](https://www.selenium.dev/) - For web browser automation.
 * [POM](https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html) - Design Pattern
 * [Allure](https://pypi.org/project/allure-pytest/) - tests execution reporting framework.

   
## To Run the tests

make sure that you installed pytest
```
pip install pytest
```
run the tests via tests file 
```
pytest tests/
```

If you want to run a specific file
```
pytest tests/fileName.py
```
## To open allure results
Allure is a open source framework for reporting the test runs.

run tests with the  ``--alluredir``  option to specify the directory where Allure should store its report data: 
```
 pytest --alluredir=reportallure
```
Generating report to temp directory
```
 allure serve .\reportallure\                                    
```
Web Server started at <http://192.168.68.50:58767/>.
            
   
## Details:

   * Pages Folder: This directory contains page object classes, making it easier to interact with web elements and encapsulating page-specific functionality
     * Base page:
                   BasePage class object serves as the foundation of a test automation framework for web applications,
                   providing a centralized location for common functionalities, encapsulating 
                   WebDriver interactions, and promoting a consistent and reusable approach to developing page objects.
                 
     * Log-in Page: This file contains a page object class for the login page,this class encapsulates the elements and functionality specific to the login page and it's same for all useres.
     * Home Page: This file contains a page object class for the home page,this class encapsulates the elements and functionality specific to the home page.
 So, After logging in, the user is redirected to the home page, from which they navigate to Evaluation page via side bar, and finally, they log out from the home page.
     * Probation Evaluation Page:  This file contains a page object class for the Evaluation page,this class encapsulates the elements and functionality specific to the home page.
       * For **HR account**, in this page there is **Probation Evaluation Table** and a **Create Evaluation** button to navigate to another page where HR click the "Create Evaluation" button to select an employee 
         and start their evaluation cycle, After the Manager/Head submitted their decision the HR confirm it and close the evaluation after the employee acknowledge it.
       * On this page, **employees** can view their probation evaluation table, which contains **their evaluations**, Once an evaluation is viewed, the employee must **acknowledge it**.
       * For **Managers**, they can view the probation evaluation table containing **evaluations of employees redirected to them**, Once an evaluation is viewed, the manager **made a decision** ( confirm 
         permanent employment in position, Extend probation period, Terminate Employment).
       * For Supervisor/ Direct Manager, they can view the **probation evaluation table containing evaluations of employees redirected to them**, Once an evaluation is viewed, the Supervisor Evaluate the employee 
         fill in the form depending in KPI's.
         
   * Tests Folder: This directory contains three test files:
       1. test_home.py: Contains a test class (TestHome) with test methods for testing functionality related to the home page (navigation between pages, log-out).
       2. test_login.py: Contains a test class (TestLogIn) with test methods positive and negative testing scenarios for login.
       3. test_evaluation.py: Contains a test class (TestEvaluation) with test methods for testing functionality and validation related to the evaluation process from three sides (HR, Manager, Employee, Direct Manager/Supervisor).
    
   * Conftest file: contain a pytest fixture, named driver  used to initialize a Selenium WebDriver instance before each test function and quits the WebDriver instance after the test function has finished running.
   * locators file: it contains definitions of locators used to identify web elements in automated tests, EvaluationLocators, LoginPageLocators,and HomePageLocators.

     
## Test Data:

* testdata.py:  contain LoginTestData, and ProbEvaluationData were test Data generated manually.
  * Login Accounts:
    * test-hr 
    * test-employee  
    * test-manager
    * test-supervisor
  * Evaluation Statuses.
  * static answer values for the fill_evaluation_form method.
* In fill_evaluation_form method checkboxes checked using **random**.
* used  @pytest.mark.parametrize for multiple sets of input parameters, to run the same test function with multiple sets of input parameters.
      
