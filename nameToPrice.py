# 종목 이름을 입력하면 네이버 금융에서 주가를 불러오는 예제

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

df = pd.read_csv("data/nameToCode.csv")
df.set_index('종목명', inplace = True)

name = input("종목명을 입력하세요: ")
if name not in df.index:
    print("종목명을 정확히 입력하세요")
else:
    print(name+"의 코드는 "+df.loc[name][0]+"입니다")
    code = df.loc[name][0]

page = requests.get("https://finance.naver.com/item/main.naver?code="+code)
soup = bs(page.text, "html.parser")

element = soup.select_one('#chart_area > div.rate_info > div > p.no_today > em > .blind') # #는 id, .은 class, 나머지는 태그, > 바로 하위 항목을 의미

print(name+"의 현 주가는 "+element.get_text()+"입니다") #텍스트만 추출