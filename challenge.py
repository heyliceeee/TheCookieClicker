from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://appbrewery.github.io/fake-newsletter-signup/" # set the URL

chrome_options = webdriver.ChromeOptions() # Create a new option object
chrome_options.add_experimental_option("detach", True) # Attach the driver to the background

driver = webdriver.Chrome(options=chrome_options) # Instantiate the driver
driver.get(URL) # Open the URL

first_name = driver.find_element(By.CSS_SELECTOR, value="#signup-form input.form-control.top") # Find the first name field
first_name.send_keys("Alice") # Enter Alice

last_name = driver.find_element(By.CSS_SELECTOR, value="#signup-form input.form-control.middle") # Find the last name field
last_name.send_keys("Dias") # Enter Dias

email = driver.find_element(By.CSS_SELECTOR, value="#signup-form input.form-control.bottom") # Find the email field
email.send_keys("alicedias2002@hotmail.com") # Enter email

submit = driver.find_element(By.CSS_SELECTOR, value="#signup-form button") # Find the Submit button
submit.click() # Click the Submit button