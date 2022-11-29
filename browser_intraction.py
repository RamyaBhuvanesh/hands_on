from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class BrowesrInteractions():
    def test(self):
        driver = webdriver.Edge()
        url1 ="https://the-internet.herokuapp.com/add_remove_elements/"
        driver.get(url1)
        driver.maximize_window()
        time.sleep(5)
        add_element_button = "//button[@onclick='addElement()']"
        click_element = driver.find_element(By.XPATH, add_element_button)
        click_element.send_keys(Keys.ENTER)
        time.sleep(2)
        click_element = driver.find_element(By.XPATH, add_element_button)
        click_element.send_keys(Keys.ENTER)
        time.sleep(2)
        click_element = driver.find_element(By.XPATH, add_element_button)
        click_element.send_keys(Keys.ENTER)
        time.sleep(2)
        click_element = driver.find_element(By.XPATH, add_element_button)
        click_element.send_keys(Keys.ENTER)
        time.sleep(2)
        click_element = driver.find_element(By.XPATH, add_element_button)
        click_element.send_keys(Keys.ENTER)
        time.sleep(2)
        delete_element = "//button[@onclick='deleteElement()']"
        click_elements = driver.find_element(By.XPATH, delete_element)
        click_elements.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.quit()

gc = BrowesrInteractions()
gc.test()
