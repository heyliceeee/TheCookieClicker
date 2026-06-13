import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://ozh.github.io/cookieclicker/" # set the URL
PURCHASE_INTERVAL = 15 # set the purchase interval in seconds
RUN_TIME = 5 * 60 # 5 minutes in seconds

chrome_options = webdriver.ChromeOptions() # Create a new option object
chrome_options.add_experimental_option("detach", True) # Attach the driver to the background

driver = webdriver.Chrome(options=chrome_options) # Instantiate the driver
driver.get(URL) # Open the URL
wait = WebDriverWait(driver, 5) # Create a new wait object

def change_language():
    """
    Change the language to English
    """
    try: # try to change the language
        wait.until(EC.presence_of_element_located((By.ID, "prompt"))) # Wait for the change language popup to appear

        lang_select = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN"))) # Wait for the language select button to be clickable
        lang_select.click() # Click the language select button

    except TimeoutException: # if the language is already set to English
        print("Language already set to English")
def click_cookie():
    """
    Click the cookie as fast as possible
    """
    cookie = driver.find_element(By.ID, "bigCookie") # find the cookie
    ActionChains(driver).click(cookie).perform() # Click the cookie


first_interaction = True # set the first interaction to true
start_time = time.time() # get the start time
last_purchase = time.time() # set the last purchase time to now
while True: # keep the game running
    if first_interaction: # if it's the first interaction
        change_language() # select english option in "change language" pop-up
        first_interaction = False # set the first interaction to false
    click_cookie()  # click the cookie as fast as possible
