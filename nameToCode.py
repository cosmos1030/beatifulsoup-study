import pandas as pd

df = pd.read_csv("data/nameToCode.csv")
df.set_index('종목명', inplace = True)
while(1):
    name = input()
    if name not in df.index:
        print("종목명을 정확히 입력하세요")
    else:
        print(name+"의 코드는 "+df.loc[name][0]+"입니다")