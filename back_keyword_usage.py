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


        # second url
        url1 = " https://www.amazon.in/"
        driver.get(url1)
        time.sleep(3)

        title_is = driver.title
        print(f"The title of the page is" + title_is)

        # go back to previous page
        driver.back()

        title_is = driver.title
        print(f"The title of the page is" + title_is)
        driver.quit()

r = Get_Title()
r.test()


