import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index{}.html'

page = 8974

for i in range(0,5):
    res = requests.get(url.format(page),headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    title_list = soup.select('div.title')

    for title_soup in title_list:
        try:
            title = title_soup.select('a')[0].text
            print(title)
            href = title_soup.select('a')[0]['href']
            print('https://www.ptt.cc' + href)
        except IndexError as e:
            print(e)
            print(title_soup)

    page-=1