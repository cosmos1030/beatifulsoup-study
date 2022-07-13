from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getElements(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        elements = soup.select('div')
    except AttributeError as e:
        return None
    return elements

elements = getElements('https://www.google.com/search?q=%EC%A0%9C%EB%84%A5%EC%8B%A0&client=ubuntu&hs=dbg&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjA8Mum__X4AhXOfHAKHclgBx4Q_AUoAXoECAIQAw&biw=1920&bih=887&dpr=1')
if elements == None:
    print('Elements could not be found')
else:
    print(elements)