from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Get_Title():

    def test(self):
        # using edge browser
        driver = webdriver.Edge()
        # url of google web page
        url = "https://www.google.com/"

        # open the url by get method
        driver.get(url)
        # rest time
        time.sleep(3)

        # maximize the window
        driver.maximize_window()
        time.sleep(3)

        # using send keys
        xpath_of_search = "//input[@name='q']"
        send_search = driver.find_element(By.XPATH, xpath_of_search)
        send_search.send_keys("guvi")
        time.sleep(4)
        send_search.send_keys(Keys.ENTER)
        time.sleep(3)

        # get the current url
        current_url = driver.current_url
        print(f" The current url is : " +current_url)

        # refresh the page
        time.sleep(3)
        driver.refresh()

        driver.quit()





r = Get_Title()
r.test()


