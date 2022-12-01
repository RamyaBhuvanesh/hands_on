from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BrowesrInteractions():
    def test(self):
        driver = webdriver.Edge()
        url1 = "https://www.google.com/"
        xpath_of_google_searchbox = "//input[@name='q']"
        xpath_of_google_searchbutton = '//input[@aria-lable="Google Search"]'
        driver.get(url1)
        driver.maximize_window()
        time.sleep(10)
        search_box = driver.find_element(By.XPATH, xpath_of_google_searchbox)
        search_box.send_keys("guvi")
        search_box.send_keys(Keys.ENTER)
        time.sleep(10)
        filename_ss = 'C:\\ss\\ss.png'
        driver.save_screenshot(filename_ss)
        driver.quit()


gc = BrowesrInteractions()
gc.test()

