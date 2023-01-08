from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from test_data import data
import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestOrangeHRM():

    url = "https://opensource-demo.orangehrmlive.com/"

    @pytest.fixture
    def bootup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(self.url)
        yield
        self.driver.quit()

    '''
   # Test Case ID: TC_PIM_01
    def test_validation_of_menuOptions(self, bootup):


        ## To check if correct webpage is displayed
        assert self.driver.title == "OrangeHRM"

        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.username_input_box_path).send_keys(data.credentials.username)
        self.driver.find_element(By.XPATH, data.element.password_input_box_path).send_keys(data.credentials.password)
        self.driver.find_element(By.XPATH, data.element.login_button_path).click()
        
        ## To check if the login was successful 
        self.driver.implicitly_wait(3)
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

        ## Open admin module
        self.driver.find_element(By.XPATH, data.element.admin_menu_path).click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.XPATH, data.element.admin_menu_path).is_displayed()
        print("Admin menu is present in the side pane")
        assert self.driver.find_element(By.XPATH, data.element.pim_menu_path).is_displayed()
        print("PIM menu is present in the side pane")
        assert self.driver.find_element(By.XPATH, data.element.leave_menu_path).is_displayed()
        print("Leave menu is present in the side pane")
        assert self.driver.find_element(By.XPATH, data.element.time_menu_path).is_displayed()
        print("Time menu is present in the side pane")
        assert self.driver.find_element(By.XPATH, data.element.recruitment_menu_path).is_displayed()
        print("Recruitment menu is present in the side pane")
        assert self.driver.find_element(By.XPATH, data.element.myinfo_menu_path).is_displayed()
        print("My info menu is present in the side pane")
        assert self.driver.find_element(By.XPATH, data.element.performance_menu_path).is_displayed()
        print("Performance menu is present in the side pane")
        assert self.driver.find_element(By.XPATH, data.element.dashboard_menu_path).is_displayed()
        print("Dashboard menu is present in the side pane")
        assert self.driver.find_element(By.XPATH, data.element.directory_menu_path).is_displayed()
        print("Directory menu is present in the side pane")
        assert self.driver.find_element(By.XPATH, data.element.maintenance_menu_path).is_displayed()
        print("Maintenance menu is present in the side pane")
        assert self.driver.find_element(By.XPATH, data.element.buzz_menu_path).is_displayed()
        print("Buzz menu is present in the side pane")

        ## Click on the Search Box and validate Menu optionsnt(By.XPATH, data.element.search_box_path).is_displayed()
        print("Search box is present in the side pane")

        ## Search for Menu options and validate reesults

        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("ADMIN")
        assert self.driver.find_element(By.XPATH, data.element.admin_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(5*Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("admin")
        assert self.driver.find_element(By.XPATH, data.element.admin_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(5*Keys.BACKSPACE)

        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("PIM")
        assert self.driver.find_element(By.XPATH, data.element.pim_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(3*Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("pim")
        assert self.driver.find_element(By.XPATH, data.element.pim_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(3*Keys.BACKSPACE)

        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("LEAVE")
        assert self.driver.find_element(By.XPATH, "//span[normalize-space()='Leave']").is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(5*Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("leave")
        assert self.driver.find_element(By.XPATH, "//span[normalize-space()='Leave']").is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(5*Keys.BACKSPACE)

        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("TIME")
        assert self.driver.find_element(By.XPATH, data.element.time_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(4*Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("time")
        assert self.driver.find_element(By.XPATH, data.element.time_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(4*Keys.BACKSPACE)
        
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("RECRUITMENT")
        assert self.driver.find_element(By.XPATH, data.element.recruitment_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(11*Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("recruitment")
        assert self.driver.find_element(By.XPATH, data.element.recruitment_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(11*Keys.BACKSPACE)

        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("MY INFO")
        assert self.driver.find_element(By.XPATH, data.element.myinfo_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(7*Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("my info")
        assert self.driver.find_element(By.XPATH, data.element.myinfo_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(7*Keys.BACKSPACE)
        
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("PERFORMANCE")
        assert self.driver.find_element(By.XPATH, "//span[normalize-space()='Performance']").is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(11*Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("performance")
        assert self.driver.find_element(By.XPATH, "//span[normalize-space()='Performance']").is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(11*Keys.BACKSPACE)

        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("DASHBOARD")
        assert self.driver.find_element(By.XPATH, data.element.dashboard_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(9*Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("dashboard")
        assert self.driver.find_element(By.XPATH, data.element.dashboard_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(9*Keys.BACKSPACE)

        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("DIRECTORY")
        assert self.driver.find_element(By.XPATH, data.element.directory_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(9*Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("directory")
        assert self.driver.find_element(By.XPATH, data.element.directory_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(9*Keys.BACKSPACE)
        
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("MAINTENANCE")
        assert self.driver.find_element(By.XPATH, data.element.maintenance_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(11*Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("maintenance")
        assert self.driver.find_element(By.XPATH, data.element.maintenance_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(11*Keys.BACKSPACE)

        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("BUZZ")
        assert self.driver.find_element(By.XPATH, data.element.buzz_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(4*Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys("buzz")
        assert self.driver.find_element(By.XPATH, data.element.buzz_menu_path).is_displayed()
        self.driver.find_element(By.XPATH, data.element.search_box_path).send_keys(4*Keys.BACKSPACE)

        print("============================================================== \n All Menu options are validated by searching!\n ==============================================================" )

    

    def test_validation_of_dropDown_pageHeaders(self, bootup):

        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.username_input_box_path).send_keys(data.credentials.username)
        self.driver.find_element(By.XPATH, data.element.password_input_box_path).send_keys(data.credentials.password)
        self.driver.find_element(By.XPATH, data.element.login_button_path).click()

        self.driver.implicitly_wait(3)
        ## Open admin module
        self.driver.find_element(By.XPATH, data.element.admin_menu_path).click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.XPATH, data.element.admin_menu_path).is_displayed()
        assert self.driver.find_element(By.XPATH, data.element.pim_menu_path).is_displayed()
        assert self.driver.find_element(By.XPATH, data.element.leave_menu_path).is_displayed()
        assert self.driver.find_element(By.XPATH, data.element.time_menu_path).is_displayed()
        assert self.driver.find_element(By.XPATH, data.element.recruitment_menu_path).is_displayed()
        assert self.driver.find_element(By.XPATH, data.element.myinfo_menu_path).is_displayed()
        assert self.driver.find_element(By.XPATH, data.element.performance_menu_path).is_displayed()
        assert self.driver.find_element(By.XPATH, data.element.dashboard_menu_path).is_displayed()
        assert self.driver.find_element(By.XPATH, data.element.directory_menu_path).is_displayed()
        assert self.driver.find_element(By.XPATH, data.element.maintenance_menu_path).is_displayed()
        assert self.driver.find_element(By.XPATH, data.element.buzz_menu_path).is_displayed()

        self.driver.find_element(By.XPATH, data.element.user_management_path).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.users_path).click()
        self.driver.implicitly_wait(3)
        default_user_role = self.driver.find_element(By.XPATH, data.element.user_role_select_path).get_attribute('innerHTML') 
        assert default_user_role == "-- Select --"
        print ("Default user role is --Select--")

        self.driver.find_element(By.XPATH, data.element.user_role_select_path).send_keys("a")
        assert self.driver.find_element(By.XPATH, data.element.user_role_select_path).get_attribute('innerHTML') == "Admin"
        self.driver.implicitly_wait(3)

        self.driver.find_element(By.XPATH, data.element.user_role_select_path).send_keys("e")
        assert self.driver.find_element(By.XPATH, data.element.user_role_select_path).get_attribute('innerHTML') == "ESS"
        
        print("Both Admin and ESS are present in the Dropdown box.")

    '''    

    #Test Case ID: TC_PM_03
    def test_create_new_employee(self, bootup):

        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.username_input_box_path).send_keys(data.credentials.username)
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.password_input_box_path).send_keys(data.credentials.password)
        self.driver.find_element(By.XPATH, data.element.login_button_path).click()
        self.driver.implicitly_wait(3)
        
        self.driver.find_element(By.XPATH, data.element.pim_menu_path).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, data.element.add_button_path).click()
        self.driver.implicitly_wait(3)

        #Check if you're in Add Employee page
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"

        action = ActionChains(self.driver)
        toggle_login_details = self.driver.find_element(By.XPATH, data.element.create_login_details_toggle_path)
        action.click(on_element=toggle_login_details)
        action.perform()
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.XPATH, data.element.first_name_path).send_keys(data.credentials.first_name)
        self.driver.find_element(By.XPATH, data.element.last_name_path).send_keys(data.credentials.last_name)
        self.driver.find_element(By.XPATH, data.element.last_name_path).send_keys(u'\ue007')
        # self.driver.find_element(By.XPATH, data.element.username_text_box_path).send_keys(data.credentials.user_name)
        # self.driver.find_element(By.XPATH, data.element.password_text_box_path).send_keys(data.credentials.pass_word)
        # self.driver.find_element(By.XPATH, data.element.confirm_password_path).send_keys(data.credentials.confirm_pass_word)
        
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.XPATH, data.element.personal_details).is_displayed()

    
