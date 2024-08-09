from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title':[], 'price':[],'link':[]}
for file in os.listdir("data"):
    try: 
        with open (f"data/{file}") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, 'html.parser')
        t = soup.find("h3")
        t = t.find("a")
        title = t['title']

        p = soup.find("p", class_="price_color")
        price = p.text
    

        l = soup.find("a")
        link = l["href"]

        print(title, "https://books.toscrape.com/catalogue/" + link[9::], price)
    except Exception as e:
        print(e)

    d["title"].append(title)
    d["price"].append(price)
    d["link"].append("https://books.toscrape.com/catalogue/" + link[9::])

    df = pd.DataFrame(data=d)
    df.to_csv("data.csv")


    

    # print(soup.prettify())