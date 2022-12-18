import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from self import self
from selenium.webdriver.common.keys import Keys

# assignment1
# Test case ID:TC_Login_01
# successful employee login to orangeHRM portal

class Successful_Employee_Login():
    def login_test():
        driver = webdriver.Chrome()

        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        time.sleep(3)

        user_name_xpath = '//input[@name="username"]'
        user_name = driver.find_element(By.XPATH, user_name_xpath).send_keys("Admin")
        time.sleep(3)
        print("user name is correct")


# assignment_2
# Test case ID:TC_Login_02
# invalid employee login to orange HRM

        password_credential = '//input[@name="password"]'
        password = driver.find_element(By.XPATH, password_credential).send_keys("admin123")
        time.sleep(5)

        print("password is correct")


        login_button_xpath = '//button[@type="submit"]'
        login = driver.find_element(By.XPATH, login_button_xpath)
        login.click()
        time.sleep(5)


# assignment_3
# Test case ID:TC_PIM_01
# add a new employee in the PIM module


        PIM_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]'
        enter_pim = driver.find_element(By.XPATH, PIM_xpath)
        enter_pim.click()
        time.sleep(3)

        add_button_xpath = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        add_button = driver.find_element(By.XPATH, add_button_xpath)
        add_button.click()
        time.sleep(3)

        first_name_xpath = '//input[@name="firstName"]'
        first_name = driver.find_element(By.XPATH, first_name_xpath)
        first_name.send_keys("Ramya")
        first_name.click()
        time.sleep(2)

        middle_name_xpath ='//input[@name="middleName"]'
        middle_name = driver.find_element(By.XPATH, middle_name_xpath)
        middle_name.send_keys("Chandrasekaran")
        middle_name.click()
        time.sleep(3)

        last_name_xpath = '//input[@name="lastName"]'
        last_name = driver.find_element(By.XPATH, last_name_xpath)
        last_name.send_keys("B")
        last_name.click()
        time.sleep(2)

        # photo_xpath = '//button[@class="oxd-icon-button employee-image-action"]'
        # photo = driver.find_element(By.XPATH, photo_xpath)
        # photo.send_keys("C:/Users/ramya/OneDrive/Pictures/Screenshots")
        # photo.click()
        # time.sleep(2)

        create_login_details_xpath = '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]'
        create_login_details = driver.find_element(By.XPATH, create_login_details_xpath)
        create_login_details.click()
        time.sleep(2)

        create_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
        create = driver.find_element(By.XPATH, create_xpath)
        create.send_keys('Ramyachan')
        create.click()
        time.sleep(2)

        password_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
        password = driver.find_element(By.XPATH, password_xpath)
        password.send_keys('Ramya123#')
        password.click()
        time.sleep(2)

        confirm_password_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
        confirm_password = driver.find_element(By.XPATH, confirm_password_xpath)
        confirm_password.send_keys('Ramya123#')
        confirm_password.click()
        time.sleep(2)

        save_data_xpath = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        save_data = driver.find_element(By.XPATH, save_data_xpath)
        save_data.click()
        time.sleep(7)

        print("succesfully saved")

        open_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'
        open = driver.find_element(By.XPATH, open_xpath)
        open.click()
        time.sleep(4)


        #xpath for Nickname
        Nickname_xpath='//label[text()="Nickname"]/following::div[1]/input'
        Nickname=driver.find_element(By.XPATH,Nickname_xpath).send_keys("puppy")
        time.sleep(4)

        #xpath for other id
        OtherID_xpath='//label[text()="Other Id"]/following::div[1]/input'
        OtherID=driver.find_element(By.XPATH,OtherID_xpath).send_keys("568790")
        time.sleep(4)

        #xpath for DL
        #DL_xpath='//label[text()="Driver's License Number"]/following::div[1]/input'
        #DL=driver.find_element(By.XPATH,DL_xpath).send_keys("158615")
        #time.sleep(4)

        #xpath for DL date
        DL_date_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
        date=driver.find_element(By.XPATH,DL_date_xpath).send_keys("2009-10-09")
        time.sleep(4)

        #xpath for SSN number
        SSN_xpath='//label[text()="SSN Number"]/following::div[1]/input'
        SSN=driver.find_element(By.XPATH,SSN_xpath).send_keys("9876")
        time.sleep(4)

        #xpath for SIN number
        SIN_xpath='//label[text()="SIN Number"]/following::div[1]/input'
        SIN=driver.find_element(By.XPATH,SIN_xpath).send_keys("567867")
        time.sleep(3)

        #xpath for Nationality
      #  Nationality_xpath=''
       # Nationality=driver.find_element(By.XPATH,Nationality_xpath).send_keys("Indian")
      #  time.sleep(3)
      #   na_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
      #   na = driver.find_element(By.XPATH, na_xpath)
      #   na.send_keys("India")
      #   na.click()
      #   time.sleep(4)
      #
      #   #xpath for Martial status
      #   Martial_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
      #   Martial=driver.find_element(By.XPATH,Martial_xpath).send_keys("Married")
      #   time.sleep(2)

        #xpath for DOB
        DOB_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
        DOB=driver.find_element(By.XPATH,DOB_xpath).send_keys("1999-05-20")
        time.sleep(3)

        #xpath for Gender
        Gender_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span'
        Gender=driver.find_element(By.XPATH,Gender_xpath).click()
        time.sleep(3)

        # blood_group_xpath ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]'
        # blood_group = driver.find_element(By.XPATH, blood_group_xpath).send_keys('B+')
        # time.sleep(3)

        #xpath to save
        Save_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
        Save=driver.find_element(By.XPATH,Save_xpath).click()
        time.sleep(5)

        # na_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
        # na = driver.find_element(By.XPATH, na_xpath)
        # na.send_keys("india")
        # na.click()
        # time.sleep(4)






# assignment_4
# Test case ID:TC_PIM_02
# edit an existing employee in the pim module











get_it = Successful_Employee_Login
get_it.login_test()
