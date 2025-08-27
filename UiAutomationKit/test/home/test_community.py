import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from pages.home.community_page import CommunityPage

class TestCommunityPage(unittest.TestCase):
    """Test suite for the Community Recipes page functionality."""

    def test_browse_community_recipes_happy_path(self):
        """Test the primary user flow for browsing recipes on the community page."""
        baseURL = "https://next-level-food-rho.vercel.app/meals"
        driver = webdriver.Safari()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(30)

        communityPage = CommunityPage(driver)
        communityPage.navigate_to_community_recipes()
        