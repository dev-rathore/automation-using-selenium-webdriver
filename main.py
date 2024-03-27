from selenium import webdriver

# Keep the chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/")

# driver.close()  # This will close the browser window
# driver.quit()  # This will close the browser window and also the driver process
