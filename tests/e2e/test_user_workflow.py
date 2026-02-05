import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

BASE_URL = "http://localhost:5000"

def test_filter_by_cuisine(driver):
    """Scenario: User filters restaurants by Cuisine Type (e.g., Italian)"""
    target_cuisine = "Italian"
    driver.get(f"{BASE_URL}/filter/cuisine?type={target_cuisine}")
    
    page_source = driver.find_element("tag name", "body").text
    data = json.loads(page_source)
    
    assert isinstance(data, list), "Response should be a list of restaurants"
    if len(data) > 0:
        assert data[0]['cuisine_type'] == target_cuisine, f"Expected {target_cuisine} results"

def test_filter_by_neighborhood(driver):
    """Scenario: User filters restaurants by Neighborhood (e.g., The Loop)"""
    target_neighborhood = "The Loop"
    driver.get(f"{BASE_URL}/filter/neighborhood?neighborhood={target_neighborhood}")
    
    page_source = driver.find_element("tag name", "body").text
    data = json.loads(page_source)
    
    assert isinstance(data, list), "Response should be a list"
    for restaurant in data:
        assert restaurant['neighborhood'] == target_neighborhood