from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class username_1():
    def name_password(self):
        driver=webdriver.Chrome()
        url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)
    #Testcase-4

        #xpath for username
        username_xpath='//input[@name="username"]'
        username=driver.find_element(By.XPATH,username_xpath).send_keys("Admin")
        time.sleep(4)

        #xpath for password
        password_xpath='//input[@name="password"]'
        password=driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
        time.sleep(4)

        #xpath for login button
        login_xpath='//button[@type="submit"]'
        submit=driver.find_element(By.XPATH,login_xpath).click()
        time.sleep(4)

        #xpath for PIM
        PIM_xpath='//a[@href="/web/index.php/pim/viewPimModule"]'
        PIM=driver.find_element(By.XPATH,PIM_xpath).click()
        time.sleep(4)

        #edit the employee details
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[5]/div').click()
        time.sleep(5)

        #xpath for Nickname
        Nickname_xpath = '//label[text()="Nickname"]/following::div[1]/input'
        Nickname = driver.find_element(By.XPATH, Nickname_xpath).send_keys(Keys.CONTROL, 'a')
        Nickname = driver.find_element(By.XPATH, Nickname_xpath).send_keys(Keys.BACKSPACE)
        Nickname = driver.find_element(By.XPATH, Nickname_xpath).send_keys("ayaan")
        time.sleep(4)

        #xpath for other id
        OtherID_xpath = '//label[text()="Other Id"]/following::div[1]/input'
        OtherID = driver.find_element(By.XPATH, OtherID_xpath).send_keys(Keys.CONTROL, 'a')
        OtherID = driver.find_element(By.XPATH, OtherID_xpath).send_keys(Keys.BACKSPACE)
        OtherID = driver.find_element(By.XPATH, OtherID_xpath).send_keys("50005")
        time.sleep(4)

        #xpath for DL
        DL_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
        DL = driver.find_element(By.XPATH, DL_xpath).send_keys(Keys.CONTROL, 'a')
        DL = driver.find_element(By.XPATH, DL_xpath).send_keys(Keys.BACKSPACE)
        DL = driver.find_element(By.XPATH, DL_xpath).send_keys("20052008")
        time.sleep(4)

        #xpath for DL date
        DL_date_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
        date = driver.find_element(By.XPATH, DL_date_xpath).send_keys(Keys.CONTROL, 'a')
        date = driver.find_element(By.XPATH, DL_date_xpath).send_keys(Keys.BACKSPACE)
        date = driver.find_element(By.XPATH, DL_date_xpath).send_keys("2030-12-18")
        time.sleep(5)

        # xpath for DOB
        DOB_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
        DOB = driver.find_element(By.XPATH, DOB_xpath).send_keys(Keys.CONTROL, 'a')
        DOB = driver.find_element(By.XPATH, DOB_xpath).send_keys(Keys.BACKSPACE)
        DOB = driver.find_element(By.XPATH, DOB_xpath).send_keys("1990-05-05")
        time.sleep(5)

        # xpath for Gender
        Gender_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        Gender = driver.find_element(By.XPATH, Gender_xpath).click()
        time.sleep(5)

        #xpath for Militaryservice
        Military_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
        MilitaryService = driver.find_element(By.XPATH, Military_xpath).send_keys(Keys.CONTROL, 'a')
        MilitaryService = driver.find_element(By.XPATH, Military_xpath).send_keys(Keys.BACKSPACE)
        MilitaryService = driver.find_element(By.XPATH, Military_xpath).send_keys("No")
        time.sleep(5)

        #xpath for Smoker
        Smoker_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label'
        Smoker = driver.find_element(By.XPATH, Smoker_xpath).send_keys("Yes")
        time.sleep(5)

        #xpath to save
        Save_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
        Save = driver.find_element(By.XPATH, Save_xpath).click()
        time.sleep(5)

a=username_1()
a.name_password()

