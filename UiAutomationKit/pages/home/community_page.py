from selenium import webdriver
from selenium.webdriver.common.by import By

class CommunityPage():
    def __init__(self, driver):
        self.driver = driver

    def  navigate_to_community_recipes(self):
        browseMeals = self.driver.find_element(By.XPATH, "/html/body/header[1]/nav/ul/li[1]/a")
        browseMeals.click()

        
