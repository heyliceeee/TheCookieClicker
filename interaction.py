from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://en.wikipedia.org/wiki/Main_Page" # set the URL

chrome_options = webdriver.ChromeOptions() # Create a new option object
chrome_options.add_experimental_option("detach", True) # Attach the driver to the background

driver = webdriver.Chrome(options=chrome_options) # Instantiate the driver
driver.get(URL) # Open the URL

articles = driver.find_element(By.CSS_SELECTOR, "#articlecount li:nth-child(2) a").text # Find the number of articles
print(articles)

driver.quit() # Quit the driver