from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class CommunityPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #locators
    browse_meals_link = "/html/body/header[1]/nav/ul/li[1]/a"

    def get_browse_meals_link(self):
        return self.driver.find_element(By.XPATH, self.browse_meals_link)
    
    def click_browse_meals_link(self):
        # self.get_browse_meals_link().click()
        self.elementClick(self.browse_meals_link, locatorType="XPATH")

    def  navigate_to_community_recipes(self):
        self.click_browse_meals_link()

    def verify_user_can_view_recipes_on_community_page(self):
        result = self.isElementPresent("/html/body/p[2]/a", locatorType="xpath")
        return result
    
    # def verify_user_can_not_view_recipes_on_community_page(self):

        
