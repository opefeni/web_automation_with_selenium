from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv


PATH = "bin/chromedriver"
driver = webdriver.Chrome(PATH)

class Scraper():
    def __init__(self, url, id) -> None:
        self.url = url
        self.id = id
        self.job_info = []

    def saveToFile(self):
        pass

    def searchUrl(self):
        search = driver.find_element(By.ID, 'searchString')
        search.send_keys(self.id)
        search.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        result = driver.find_element(By.CLASS_NAME, "results-jobs")
        result.click()
        driver.implicitly_wait(10)