import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from self import self
from selenium.webdriver.common.keys import Keys


class Successful_Employee_Login():
    def login_test(self):
       driver = webdriver.Chrome()

       url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
       driver.get(url)
       time.sleep(3)

       user_name_xpath = '//input[@name="username"]'
       user_name = driver.find_element(By.XPATH, user_name_xpath)
       user_name.send_keys("Admin")
       time.sleep(3)

       password_credential = '//input[@name="password"]'
       password = driver.find_element(By.XPATH, password_credential)
       password.send_keys("admin123")
       print(password)
       time.sleep(5)

       login_button_xpath = '//button[@type="submit"]'
       login = driver.find_element(By.XPATH, login_button_xpath)
       login.click()
       time.sleep(5)











get_it = Successful_Employee_Login
get_it.login_test(self)

