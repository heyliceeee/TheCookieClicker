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
def get_price(product):
    """
    Get the price of a product
    :param product: item
    :return: price as a float
    """
    try: # try to get the price
        price_el = product.find_element(By.CLASS_NAME, "price") # Find the price element
        price_text = price_el.text.replace(",", "") # Get the text content of the price element
        return float(price_text) # Return the price as a float
    except: # if the price is not found
        return 999999999
def purchase_items():
    """
    Purchase the most expensive item
    """
    cookies_text = driver.find_element(By.ID, "cookies").text.split(" ")[0] # Get the text content of the cookies element
    cookies = float(cookies_text.replace(",", "")) # Convert the text content to a float
    if cookies < 200: # if there are not enough cookies
        return # stop looking for other products

    products = driver.find_elements(By.CSS_SELECTOR,"#products .product.unlocked.enabled") # Find all the available products
    if not products: # if there are no available products
        return # stop looking for other products

    products_sorted = sorted(products, key=get_price, reverse=True) # sort the products by price
    products_sorted[0].click() # Click the most expensive product
def purchase_upgrades():
    """
    Purchase all the upgrades
    """
    upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades .upgrade.enabled") # Find all the upgrades
    for up in upgrades: # loop through the upgrades
        up.click() # Click the upgrade

first_interaction = True # set the first interaction to true
start_time = time.time() # get the start time
last_purchase = time.time() # set the last purchase time to now
while True: # keep the game running
    if first_interaction: # if it's the first interaction
        change_language() # select english option in "change language" pop-up
        first_interaction = False # set the first interaction to false
    click_cookie()  # click the cookie as fast as possible

    if time.time() - last_purchase >= PURCHASE_INTERVAL:  # if it's time to buy an upgrade
        purchase_upgrades()  # buy all the upgrades
        purchase_items()  # buy the cheapest upgrade
        last_purchase = time.time()  # update the last purchase time