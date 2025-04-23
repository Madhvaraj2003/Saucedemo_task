import pytest                                                            # Importing pytest. 
from selenium import webdriver                                           # Using selenium to get the web access.
from selenium.webdriver.common.by import By

@pytest.fixture                                                          # Using fuxture method.
def driver():
    driver = webdriver.Chrome()                                          # Setting up web browser.
    yield driver 
    driver.quit()

def test_title(driver):                                                  # Testing title.
    driver.get("https://www.saucedemo.com/") 
    assert "Swag Labs" in driver.title  


def test_homepage_url(driver):                                           # Testing the homepage.  
    driver.get("https://www.saucedemo.com/")
    assert driver.current_url == "https://www.saucedemo.com/"

def test_login_and_dashboard_url(driver):
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element( By.ID, "user-name").send_keys("standard_user") # Used to get information from web.

    driver.find_element( By.ID, "password").send_keys("secret_sauce") 
    
    driver.find_element( By.ID, "login-button"). click()

    assert "inventory.html" in driver.current_url

def test_invalid_login(driver):                                         # Testing one negative test case. using invalid credentials.
        
        driver.find_element( By.ID, "user-name").send_keys("standard_user") 

        driver.find_element( By.ID, "password").send_keys("secret_sauce") 
    
        driver.find_element( By.ID, "login-button"). click()

        error  = driver.find_element(By.CLASS_NAME, "error-message-container").text   # Error message to show.
        assert "Epic sad face invalid login"

