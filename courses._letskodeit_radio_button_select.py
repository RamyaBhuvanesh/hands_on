from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Get_Rbutton():

    def test(self):
        # using edge browser
        driver = webdriver.Edge()
        # url of google web page
        url = "https://courses.letskodeit.com/practice"

        # open the url by get method
        driver.get(url)
        # rest time
        time.sleep(3)

        # maximize the window
        driver.maximize_window()
        time.sleep(3)

        xpath_of_radio_button = '//*[@id="bmwradio"]'
        select_the_button = driver.find_element(By.XPATH, xpath_of_radio_button)
        select_the_button.click()
        time.sleep(3)

        text = select_the_button.text

        print(f"the radio button name is : " + text)


r = Get_Rbutton()
r.test()