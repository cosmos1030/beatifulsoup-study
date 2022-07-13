import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

page = requests.get("https://www.google.com/search?q=%EC%A0%9C%EB%84%A5%EC%8B%A0&client=ubuntu&hs=dbg&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjA8Mum__X4AhXOfHAKHclgBx4Q_AUoAXoECAIQAw&biw=1920&bih=887&dpr=1")
soup = bs(page.text, "html.parser")
elements = []
print(soup.select(".nDgy9d"))
for i in range(1,11):
    element = soup.select_one("div.mCBkyc.y355M.ynAwRc.MBeuO.nDgy9d")
    elements.append(element)
print(elements)