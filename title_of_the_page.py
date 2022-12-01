from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Get_Title():

    def test(self):
        driver = webdriver.Edge()
        url = "https://www.google.com/"

        driver.get(url)

        time.sleep(3)

        driver.maximize_window()
        time.sleep(3)

        title_is = driver.title
        print(f"The title of the page is" + title_is)

r = Get_Title()
r.test()


