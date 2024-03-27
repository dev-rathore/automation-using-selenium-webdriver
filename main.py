from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.in/Nikon-20-9MP-Camera-18-140mm-3-5-5-6G/dp/B06Y5RTN1T/")

# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(f"Price: {price.text} rupees")

driver.get("https://www.youtube.com/")
search_box = driver.find_element(By.NAME, value="search_query")
print(search_box.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="search-icon-legacy")
print(button.tag_name)

# find element by css selector
# search_box2 = driver.find_element(By.CSS_SELECTOR, value="input#search")
# search_box2 = driver.find_element(By.CSS_SELECTOR, value=".ytd-searchbox p")
# print(search_box2.tag_name)

# find element by xpath
# Copy the xpath from the browser's inspect element and paste it here
# search_box3 = driver.find_element(By.XPATH, value="//input[@id='search']")
# print(search_box3.tag_name)

# driver.close()  # This will close the browser window
driver.quit()  # This will close the browser window and also the driver process
