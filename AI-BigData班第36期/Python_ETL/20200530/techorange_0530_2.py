import requests
import json
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

data ={'action': 'fm_ajax_load_more','nonce': 'd8c08f1381','page': '1'}

res = requests.post(url=url,headers=headers,data=data)
json_data = json.loads(res.text)

# print(json_data)
# print(json_data.keys())
# print(json_data['data'])# html string

soup = BeautifulSoup(json_data['data'],'html.parser')
title_list = soup.select('a[class="post-thumbnail nljf"]')
for t in title_list:
    print(t)
    print(t['onclick'].split(',')[4])