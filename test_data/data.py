## This file contains all the data required for the scripts to run.
## Please make necessary changes to this file as needed.

class credentials:

    username = "Admin"
    password = "admin123"
    ## Invalid password
    invalid_password = "invalid_password"

    ## Employee Information
    first_name = "Anon"
    last_name = "Joe"
    
class element:

    ## Relative path for Username input box
    username_input_box_path = "//input[@placeholder='Username']"

    ## Relative path for Username input box
    password_input_box_path = "//input[@placeholder='Password']"

    ## Relative path for Login button
    login_button_path = "//button[@type='submit']"

    ## Relative path for Dashboard text
    Dashboard_text_path = "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']]"

    ## Invalid credentials text
    invalid_credentials_path = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    ## Employee Informations
    pim_module_path = "oxd-main-menu-item active" #class

    ## Add button in PIM
    add_button_path = "//button[normalize-space()='Add']"

    first_name_path = "//input[@placeholder='First Name']"
    last_name_path = "//input[@placeholder='Last Name']"

    ## Save after adding details
    save_button_path = "//button[@type='submit']"

    ## Name of the employee in portal
    profile_name_path = "//h6[@class='oxd-text oxd-text--h6 --strong']"

    ## Edit employee
    edit_employee_path = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]"
    middle_name_path = "//input[@placeholder='Middle Name']"
    save_change_path = "//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']"
    success_message_path = "//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']"

    ## Delete employee
    delete_employee_path = "//div[@role='table']//div[1]//div[1]//div[9]//div[1]//button[1]//i[1]"
    confirm_delete_path = "//button[normalize-space()='Yes, Delete']"
    delete_success_message_path = "//div[@class='oxd-toast-content oxd-toast-content--success']"

    