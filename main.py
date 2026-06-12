from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://www.python.org" # set the URL

chrome_options = webdriver.ChromeOptions() # Create a new option object
chrome_options.add_experimental_option("detach", True) # Attach the driver to the background

driver = webdriver.Chrome(options=chrome_options) # Instantiate the driver
driver.get(URL) # Open the URL

items = driver.find_elements(By.CSS_SELECTOR, ".shrubbery ul.menu li") # Find all the items
events = {}
i=0
for li in items: # Loop through the items
    times = li.find_elements(By.TAG_NAME, "time") # Find all the times
    if not times: # If there are no times
        continue # Skip this item

    date = times[0].text # Get the date
    a = li.find_element(By.TAG_NAME, "a") # Find the link
    title = a.text # Get the title

    events[i] = {"time": date, "name": title} # Add the event to the list
    i+=1

print(events)

# try: # Try to click the button
#     btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.a-button-text"))) # Wait for the button to be clickable
#     ActionChains(driver).move_to_element(btn).click().perform()  # Click the button
#     print("Button clicked")
#
# except: # If the button is not found
#     print("Button not found")
#
#
# try: # now try to get the price
#     price_euro = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))) # Wait for the price element to appear
#     price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")  # Find the price element
#     print(price_euro.text + "." + price_cents.text)
#
# except: # If the price is not found
#     print("Price not found")

#driver.close() # Close the driver
driver.quit() # Quit the driver