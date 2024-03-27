from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.youtube.com/")
search_box = driver.find_element(By.NAME, value="search_query")
print(search_box.tag_name)
search_box.send_keys("Avengers Endgame", Keys.ENTER)

# find element by link text
# trending_link = driver.find_element(By.LINK_TEXT, value="Trending")
# trending_link.click()

# driver.quit()
