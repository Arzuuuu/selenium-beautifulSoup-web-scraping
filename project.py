from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# import time

driver = webdriver.Chrome()
query = "historical-fiction_4"
file = 0
for i in range(1,3):
    driver.get(f"https://books.toscrape.com/catalogue/category/books/{query}/page-{i}.html")
    elems = driver.find_elements(By.CLASS_NAME, "product_pod")

# print(elems)
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
        file+=1
        # print(elem.text)
        # print("")
# print(elem.text)
# print(elem.get_attribute("outerHTML"))
 
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("Python")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# time.sleep(6)
    # time.sleep(1)
driver.close()