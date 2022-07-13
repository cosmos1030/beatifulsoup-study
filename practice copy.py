import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

page = requests.get("https://www.google.com/search?q=%EC%A0%9C%EB%84%A5%EC%8B%A0&client=ubuntu&hs=dbg&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjA8Mum__X4AhXOfHAKHclgBx4Q_AUoAXoECAIQAw&biw=1920&bih=887&dpr=1")
soup = bs(page.text, "html.parser")

element = soup.select_one('#rso > div:nth-child(6) > div > a > div > div.iRPxbe > div.mCBkyc.y355M.ynAwRc.MBeuO.nDgy9d')

print(element.get_text())