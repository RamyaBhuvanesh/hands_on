from selenium import webdriver
from selenium.webdriver.edge.options import Options

url = "https://www.guvi.in"



def ramya_headless_browser(url):
    options = Options()
    options.headless = True
    driver = webdriver.Edge(options=options)
    driver.get(url)
    print(driver.title)
    print(driver.current_url)
    driver.close()


ramya_headless_browser(url)
