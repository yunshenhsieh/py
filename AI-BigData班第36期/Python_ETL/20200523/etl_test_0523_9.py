import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

url = 'http://e5918cb4.ngrok.io/practice/100'


ss = requests.session()

res = ss.get(url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
# 這題的重點在hidden的value會隨時間改變，跟cookies有些關聯，所以一定要用session帶值，這樣才會夠快，下面就是用session帶值
key = soup.select('input')[1]['name']
value = soup.select('input')[1]['value']
#有發現value會一直改變，但我是用手key上去，所以一定來不及，才一直失敗。
data = {key : value,'pwd':'隨便打，不重要，根本沒檢查'}
res = ss.post(url,headers=headers,data=data)
print(res.text)