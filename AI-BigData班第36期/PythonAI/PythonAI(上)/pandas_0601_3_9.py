import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
df=pd.read_json('https://bit.ly/2Qfzovb')
df["UVI"]=pd.to_numeric(df["UVI"])
df=df.sort_values(by="UVI",ascending=False)
df=df.drop(columns=["SiteName"])
df=df.rename(columns={"County":"城市","PublishTime":"發布時間","UVI":"紫外線指數"})
df=df.reset_index(drop=True)
print(df.head(5))