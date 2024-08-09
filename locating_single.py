from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "travel_2"
driver.get(f"https://books.toscrape.com/catalogue/category/books/{query}/index.html")
elem = driver.find_element(By.CLASS_NAME, "product_pod")
print(elem.text)
print(elem.get_attribute("outerHTML"))
time.sleep(4)
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("Python")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# time.sleep(6)
driver.close()