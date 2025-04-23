from selenium import webdriver                                            # used to setup the webdriver.
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()                                               # Using chrome for getting the data.                                    
driver.get("https://www.saucedemo.com/")
driver.find_element( By.ID, "user-name").send_keys("standard_user")       # Here we find the all the elements which we want to access.
driver.find_element( By.ID, "password").send_keys("secret_sauce") 
driver.find_element( By.ID, "login-button"). click()
time.sleep(3)
print("Page Title:", driver.title)                                        # Used to print the statements.
print("Current_URL:", driver.current_url)

with open("Webpage_Task_11.txt", "w", encoding='utf-8') as file: file.write(driver.page_source)  # Getting the content from that website in html form.

driver.quit()                                                             # Returning from the website.
