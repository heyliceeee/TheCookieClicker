from selenium import webdriver

chrome_options = webdriver.ChromeOptions() # Create a new option object
chrome_options.add_experimental_option("detach", True) # Attach the driver to the background

driver = webdriver.Chrome(options=chrome_options) # Instantiate the driver
driver.get("https://www.amazon.com") # Open the browser

#driver.close() # Close the driver
#driver.quit() # Quit the driver