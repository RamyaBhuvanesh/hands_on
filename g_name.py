from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BrowesrInteractions():
    def test(self):
        driver = webdriver.Edge()
        url1 = "https://www.google.com"
        driver.get(url1)
        driver.maximize_window()
        time.sleep(3)
        search = "//input[@name='q']"
        element = driver.find_element(By.XPATH, search)
        element.send_keys("ramya")
        element.send_keys(Keys.ENTER)
       
g = BrowesrInteractions()
g.test()
