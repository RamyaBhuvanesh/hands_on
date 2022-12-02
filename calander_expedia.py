import bdb

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Calender_Selection():
    def test(self):
        driver = webdriver.Edge()
        '''
        
        1. open expedia.com
        2. switch to flights tab
        3, switch one way tab
        4. open calender
        5. click on specific date
        
        '''
        # get url of expedia
        url = 'https://www.expedia.com/'
        driver.get(url)

        # maximize the window
        driver.maximize_window()

        # shift to flight
        xpath_of_fight ='//a[@href="?pwaLob=wizard-flight-pwa"]'
        switch_fight = driver.find_element(By.XPATH, xpath_of_fight)
        switch_fight.click()
        time.sleep(3)

        # switch to oneway
        one_way_xpath = '//a[@href="?flightType=oneway"]'
        oneway = driver.find_element(By.XPATH, one_way_xpath)
        oneway.click()
        time.sleep(3)

        # calender selection
        cal_id='//button[@id="d1-btn"]'
        cal = driver.find_element(By.ID, 'd1-btn')
        cal.click()
        time.sleep(3)

        # choose the date
        select_date_path = '//button[@aria-label="Dec 9, 2022"]'
        selected_date = driver.find_element(By.XPATH, select_date_path)
        selected_date.click()
        time.sleep(3)

        # done option select
        xpath_for_done = '//button[@data-stid="apply-date-picker"]'
        done = driver.find_element(By.XPATH, xpath_for_done)
        done.click()
        time.sleep(3)

B = Calender_Selection()
B.test()