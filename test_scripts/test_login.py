from selenium import webdriver
from selenium.webdriver.common.by import By
from test_data import data
import time
import pytest

class TestOrangeHRM():

    url = "https://opensource-demo.orangehrmlive.com/"

    @pytest.fixture
    def bootup(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.quit()


    # Test Case ID: TC_Login_01 (Succesful Login)
    def test_login(self, bootup):
        self.driver.get(self.url)

        ## To check if correct webpage is displayed
        assert self.driver.title == "OrangeHRM"

        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.username_input_box_path).send_keys(data.credentials.username)
        self.driver.find_element(By.XPATH, data.element.password_input_box_path).send_keys(data.credentials.password)
        self.driver.find_element(By.XPATH, data.element.login_button_path).click()
        self.driver.implicitly_wait(3)

        ## To check if the login was successful 
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        

    # Test Case ID: TC_Login_01 (Succesful Login)
    def test_login(self, bootup):
        self.driver.get(self.url)

        ## To check if correct webpage is displayed
        assert self.driver.title == "OrangeHRM"

        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.username_input_box_path).send_keys(data.credentials.username)
        self.driver.find_element(By.XPATH, data.element.password_input_box_path).send_keys(data.credentials.password)
        self.driver.find_element(By.XPATH, data.element.login_button_path).click()
        self.driver.implicitly_wait(3)

        ## To check if the login was successful 
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        

    # Test Case ID: TC_Login_02 (Unsuccessful Login)
    def test_invalid_login(self, bootup):
        self.driver.get(self.url)
        assert self.driver.title == "OrangeHRM"   # Test Case ID: TC_Login_02
    def test_invalid_login(self, bootup):
        self.driver.get(self.url)
        assert self.driver.title == "OrangeHRM"

        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.username_input_box_path).send_keys(data.credentials.username)
        self.driver.find_element(By.XPATH, data.element.password_input_box_path).send_keys(data.credentials.invalid_password)
        self.driver.find_element(By.XPATH, data.element.login_button_path).click()

        ## To check if the login was unsuccessful
        time.sleep(5)
        assert self.driver.find_element(By. XPATH, data.element.invalid_credentials_path).is_displayed()
        message = self.driver.find_element(By. XPATH, data.element.invalid_credentials_path).text
        print("Error Message for Invalid Login ", message)

    # Test Case ID: TC_Login_02 (Unsuccessful Login)
    def test_invalid_login(self, bootup):
        self.driver.get(self.url)
        assert self.driver.title == "OrangeHRM"   # Test Case ID: TC_Login_02
    def test_invalid_login(self, bootup):
        self.driver.get(self.url)
        assert self.driver.title == "OrangeHRM"

        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.username_input_box_path).send_keys(data.credentials.username)
        self.driver.find_element(By.XPATH, data.element.password_input_box_path).send_keys(data.credentials.invalid_password)
        self.driver.find_element(By.XPATH, data.element.login_button_path).click()

        ## To check if the login was unsuccessful
        time.sleep(5)
        assert self.driver.find_element(By. XPATH, data.element.invalid_credentials_path).is_displayed()
        message = self.driver.find_element(By. XPATH, data.element.invalid_credentials_path).text
        print("Error Message for Invalid Login ", message)

   # Test Case ID: TC_PIM_01
    def test_add_employee(self, bootup):
        self.driver.get(self.url)

        ## To check if correct webpage is displayed
        assert self.driver.title == "OrangeHRM"

        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.username_input_box_path).send_keys(data.credentials.username)
        self.driver.find_element(By.XPATH, data.element.password_input_box_path).send_keys(data.credentials.password)
        self.driver.find_element(By.XPATH, data.element.login_button_path).click()
        
        ## To check if the login was successful 
        self.driver.implicitly_wait(3)
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        ## Open pim module
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPimModule")
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.add_button_path).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, data.element.first_name_path).send_keys(data.credentials.first_name)
        self.driver.find_element(By.XPATH, data.element.last_name_path).send_keys(data.credentials.last_name)
        self.driver.find_element(By.XPATH, data.element.save_button_path).click()
        time.sleep(5)

        ## To check if the employee was added
        assert self.driver.find_element(By.XPATH, data.element.profile_name_path).text == data.credentials.first_name + " " + data.credentials.last_name

 
    # Test Case ID: TC_PIM_02
    def test_edit_employee(self, bootup):
        self.driver.get(self.url)

        ## To check if correct webpage is displayed
        assert self.driver.title == "OrangeHRM"

        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.username_input_box_path).send_keys(data.credentials.username)
        self.driver.find_element(By.XPATH, data.element.password_input_box_path).send_keys(data.credentials.password)
        self.driver.find_element(By.XPATH, data.element.login_button_path).click()
        
        ## To check if the login was successful 
        self.driver.implicitly_wait(3)
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        ## Open pim module
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPimModule")
        self.driver.implicitly_wait(5)

        ## To edit employee details
        self.driver.find_element(By.XPATH, data.element.edit_employee_path).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, data.element.middle_name_path).send_keys("John")
        self.driver.find_element(By.XPATH, data.element.save_button_path).click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.XPATH, data.element.success_message_path).is_enabled()

    # Test Case ID: TC_PIM_03
    def test_delete_employee(self, bootup):
        self.driver.get(self.url)

        ## To check if correct webpage is displayed
        assert self.driver.title == "OrangeHRM"

        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.username_input_box_path).send_keys(data.credentials.username)
        self.driver.find_element(By.XPATH, data.element.password_input_box_path).send_keys(data.credentials.password)
        self.driver.find_element(By.XPATH, data.element.login_button_path).click()
        
        ## To check if the login was successful 
        self.driver.implicitly_wait(3)
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        ## Open pim module
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPimModule")
        self.driver.implicitly_wait(5)

        ## To delete employee
        self.driver.find_element(By.XPATH, data.element.delete_employee_path).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, data.element.confirm_delete_path).click()
        self.driver.implicitly_wait(10)
        assert self.driver.find_element(By.XPATH, data.element.delete_success_message_path).is_enabled()