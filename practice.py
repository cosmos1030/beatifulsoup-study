import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

page = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%A0%9C%EB%84%A5%EC%8B%A0")
soup = bs(page.text, "html.parser")

element = soup.select_one('#_cs_root > div.ar_spot > div > h3 > a > span.spt_con.up > strong')

print(element.get_text())