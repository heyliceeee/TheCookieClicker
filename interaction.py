from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page" # set the URL

chrome_options = webdriver.ChromeOptions() # Create a new option object
chrome_options.add_experimental_option("detach", True) # Attach the driver to the background

driver = webdriver.Chrome(options=chrome_options) # Instantiate the driver
driver.get(URL) # Open the URL

number_of_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount li:nth-child(2) a") # Find the number of articles
#number_of_articles.click() # Click the number of articles

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals") # Find the content portals link

search = driver.find_element(By.NAME, value="search") # Find the search box
search.send_keys("Python", Keys.ENTER) # Search for Python

driver.quit() # Quit the driver