from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://www.amazon.com/Wireless-Carplay-Portable-Android-Navigation/dp/B0H1VJYJ1D/ref=sr_1_3?crid=3CM7L4RY74P1A&dib=eyJ2IjoiMSJ9.DWJWSg1d0zVRVQ9YmrpGLFNcthdvn8HCUUI99aACWuqBP3Y0KQaLB2COLZN3NxvHru-WWh8cWdnRGANCUJ4hye2crs_8Zsx4KS173rYkqHezyy8_EEC9MrWbA4sFgK-PJhptd_BT1QQrKvx8aLTgPv7n_mpdbTbYx2jKY-cMDuMohz49ZgYHQlfrI48YrgMoHFbrQMMuUH0t-E6nBfERUnv1LPdR9jU89HcjD10kfNw.r8KppV_rVtNXaEFCuQIHBH_Uj356ryE2r26--CAFEQU&dib_tag=se&keywords=carplay%2Bscreen%2BCAMERA&qid=1781187360&sprefix=carplay%2Bscreen%2Bcamera%2Caps%2C304&sr=8-3&th=1" # set the URL

chrome_options = webdriver.ChromeOptions() # Create a new option object
chrome_options.add_experimental_option("detach", True) # Attach the driver to the background

driver = webdriver.Chrome(options=chrome_options) # Instantiate the driver
driver.get(URL) # Open the URL

wait = WebDriverWait(driver, 10) # Create a new wait object
try: # Try to click the button
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.a-button-text"))) # Wait for the button to be clickable
    ActionChains(driver).move_to_element(btn).click().perform()  # Click the button
    print("Button clicked")

except: # If the button is not found
    print("Button not found")


try: # now try to get the price
    price_euro = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))) # Wait for the price element to appear
    price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")  # Find the price element
    print(price_euro.text + "." + price_cents.text)

except: # If the price is not found
    print("Price not found")

#driver.close() # Close the driver
driver.quit() # Quit the driver