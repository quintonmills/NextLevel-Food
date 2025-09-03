from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from pages.home.community_page import CommunityPage

class RecipePage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    share_recipes_link = "/html/body/p[2]/a"
    name_field = "//*[@id='name']"
    email_field = "//*[@id='email']"
    title_field = "//*[@id='title']"
    summary_field="//*[@id='summary']"
    instructions_field = "//*[@id='instructions']"
    share_button = '/html/body/main/form/p[4]/button'
    # upload_image_link = '/html/body/main/form/div[2]/div/button'
    # image_path = '/Users/quinton/Documents/NextLevel-Food/UiAutomationKit/Omelet_With_Fixings.jpg'

    def navigate_to_share_recipes_screen(self):
        communityPage = CommunityPage(self.driver)
        communityPage.navigate_to_community_recipes()
        self.elementClick(self.share_recipes_link, locatorType="XPATH")

    def enter_credentials(self, name, email):
        self.sendKeys(name, self.name_field, locatorType="XPATH")
        self.sendKeys(email, self.email_field, locatorType="XPATH")

    def enter_recipe(self, title, summmary, instructions):
        self.sendKeys(title, self.title_field, locatorType="XPATH")
        self.sendKeys(summmary, self.summary_field, locatorType="XPATH")
        self.sendKeys(instructions, self.instructions_field, locatorType="XPATH")
    def click_submit_link(self):
        self.elementClick(self.share_button, locatorType="XPATH")

    def share_recipe(self, name, email, title, summary, instructions):
        """
        Complete recipe sharing workflow in one method
        
        Args:
            name: User's name
            email: User's email
            title: Recipe title
            summary: Recipe summary
            instructions: Recipe instructions
        """
        self.navigate_to_share_recipes_screen()
        self.enter_credentials(name, email)
        self.enter_recipe_details(title, summary, instructions)
        self.click_submit()
    # def upload_recipe_image(self, image_file_path):
    #      """
    #     Uploads an image by sending the file path directly to the input element.
        
    #     Args:
    #         absolute_file_path (str): The full system path to the image file.
    #                                   Example: "/Users/yourname/Projects/test-image.jpg"
    #     """
    #      self.sendKeys(image_file_path, self.image_path, locatorType="css")

    # def verify_user_can_share_recipe(self):
    #     result = self.isElementPresent("/html/body/p[2]/a", locatorType="xpath")
    #     return result
        


