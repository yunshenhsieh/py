import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

url = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'

ss = requests.session()
print(ss.cookies)
# All request put in seesion
# session 1 start
# res = requests.get(url,headers=headers)
res = ss.get(url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
button = soup.select('button[class="btn-big"]')[0]
print(button)
print(button['name'])
print(button['value'])
print(ss.cookies)

# 老師建議以後有看到多少input就帶多少資料進去，這次只是ptt八卦版可以不用帶hidden的input也可以進，所以我們沒有帶還是可以成功。
hidden = soup.select('input')
print(hidden)

data = {}
data[button['name']] = button['value']
for k in hidden:
    data[k['name']] = k['value']
print(data)

# session 2 start
target_url = 'https://www.ptt.cc/ask/over18'
# res_target= requests.post(target_url,data=data,headers=headers)
res_target = ss.post(target_url,data=data,headers=headers)
print(ss.cookies)

# session 3 start
final_url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
# final_res = requests.get(final_url,headers=headers)
final_res = ss.get(final_url,headers=headers)
# print(final_res.text)
print(ss.cookies)