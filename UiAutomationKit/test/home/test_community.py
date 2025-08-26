import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCommunityPage():
    """Test suite for the Community Recipes page functionality."""

    def test_browse_community_recipes_happy_path(self):
        """Test the primary user flow for browsing recipes on the community page."""
        baseURL = "https://next-level-food-rho.vercel.app/meals"
        driver = webdriver.Safari()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(30)

        browseMeals = driver.find_element(By.XPATH, "/html/body/header[1]/nav/ul/li[1]/a")
        browseMeals.click()

        mealsButton = driver.find_element(By.XPATH, "/html/body/p[2]/a")
        if mealsButton is not None:
            time.sleep(3)
            print('navigation successful')
            
        else:
            print('navigation not successful')

ff = TestCommunityPage()
ff.test_browse_community_recipes_happy_path()


