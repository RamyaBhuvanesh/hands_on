"""
1. selenium -
2. range - function
3. file handling -
excercise  - url.txt
open google - indian cricket team
1. https://twitter.com/search/indian+cricket+team
2. Wikipediahttps://en.wikipedia.org › wiki › India_national_cricket
3. www.link3
4. www.link4
5. www.link5
"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def range_example() :


    # range function tkaes 3 arguments range(start=,stop=,skip=) :
    # start is included
    # stop is excluded
    # skip is for
    # interview question  - difference bw range and xrange

    h_list = ['https://en.wikipedia.org/wiki/India_national_cricket_team', 'https://www.espncricinfo.com/team/india-6',
     'https://twitter.com/BCCI?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor',
     'https://www.business-standard.com/article/sports/rohit-sharma-is-number-1-cricketer-of-india-says-team-india-chief-selector-122021900711_1.html',
     'https://www.realbuzz.com/articles-interests/sports-activities/article/cricket-fielding-positions-and-players/',
     'https://www.bcci.tv/players/men', 'https://www.bcci.tv/', 'https://www.instagram.com/indiancricketteam/?hl=en',
     'https://www.facebook.com/IndianCricketTeam/', 'https://www.icc-cricket.com/teams/men/14/india/overview',
     'https://sports.ndtv.com/cricket/teams/6-india-teamprofile']

    filename_1 = 'url.txt'
    with open(filename_1,mode = "w") as writer_object :
        for i in range(1,7) :
            writer_object.write(f"{i}. {h_list[i]} \n")


def assignement2() :
    # empty list
    href_link1 = []
    # open the webpage to base url
    baseurl = "https://www.google.com/"
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(baseurl)

    # search and enter of the term "indian cricket team "
    xpath_for_google_search_text = '//input[@name="q"]'
    google_search = driver.find_element(By.XPATH, xpath_for_google_search_text)
    google_search.send_keys("india cricket team")
    google_search.send_keys(Keys.ENTER)

    time.sleep(2)
    # # 1st link

    xpath_of_all_elements_withLink = '//a[@href]//h3//parent::a'

    list_of_web_elements_having_url = driver.find_elements(By.XPATH, xpath_of_all_elements_withLink)

    for elem in list_of_web_elements_having_url:
        l = elem.get_attribute("href")
        if l not in href_link1:
            href_link1.append(l)

    filename_1 = 'url.txt'
    with open(filename_1,mode = "w") as writer_object :
        for i in range(1,7) :
            writer_object.write(f"{i}. {href_link1[i]} \n")

    driver.close()

assignement2()
# range_example()