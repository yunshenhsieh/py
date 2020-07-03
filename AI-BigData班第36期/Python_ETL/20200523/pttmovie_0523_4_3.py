import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index.html'

for i in range(0,5):
    res = requests.get(url,headers=headers)
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

    #Get last-page url
    page_url_soup = soup.select('a[class="btn wide"]')
    last_page_url = 'https://www.ptt.cc' + page_url_soup[1]['href']
    url = last_page_url