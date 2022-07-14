# %%
import pandas as pd

# %%
df1 = pd.read_csv("data/코스닥.csv")
df2 = pd.read_csv("data/코스피.csv")
# %%
df1.head()
# %%
df1 = df1.iloc[:, [0,1]]
# %%
df1
# %%
df2 = df2.iloc[:, [0,1]]
# %%
df2
# %%
df = pd.concat([df1,df2])
df
# %%
df.set_index('종목명', inplace = True)
# %%
df.head()
# %%
df.info()
# %%
df.loc['삼성전자'][0]
# %%
df.to_csv("data/nameToCode.csv", mode='w')

# %%
