from pathlib import Path
import unittest
from selenium import webdriver
from pages.recipes.submit_recipe_page import RecipePage

class TestSubmitRecipe(unittest.TestCase):
    """Test suite for the Recipe Submission functionality."""

    def test_submit_new_recipe_happy_path(self):
        """Test that a user can successfully submit a new recipe."""
        baseURL = "https://next-level-food-rho.vercel.app/meals/share" 
        driver = webdriver.Safari()
        driver.maximize_window()
        driver.get(baseURL)

        recipePage = RecipePage(driver)
        recipePage.navigate_to_share_recipes_screen()
        recipePage.enter_credentials('Quinton', 'test@test.com')
        recipePage.enter_recipe('omelette', 'egg dish', 'cook until done')
        recipePage.click_submit_link()