import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists('C:\\Users\\Big data\\Desktop\\pttmovie'):
    os.mkdir('C:\\Users\\Big data\\Desktop\\pttmovie')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index.html'
n=0
for i in range(0,5):
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    title_list = soup.select('div.title')

    for title_soup in title_list:
        try:
            title = title_soup.select('a')[0].text

            href = 'https://www.ptt.cc' + title_soup.select('a')[0]['href']

            #Get article content
            res_article = requests.get(href, headers=headers)
            soup_article = BeautifulSoup(res_article.text, 'html.parser')
            article_content_list = soup_article.select('#main-content')
            article_content = article_content_list[0].text.split('※ 發信站')[0]
            print(href)
            print(title)
            # print(article_content)
            n+=1

            try:
                with open('C:\\Users\\Big data\\Desktop\\pttmovie\\%s.txt' %(str(n) + title.replace('/','-')),'w',encoding='utf-8') as f:
                    f.write(article_content)
            except FileNotFoundError as e:
                print(e)
                print(title)
            except OSError as e:
                title=title.replace('?','')

        except IndexError as e:
            print(e)
            print(title_soup)

    #Get last-page url
    page_url_soup = soup.select('a[class="btn wide"]')
    last_page_url = 'https://www.ptt.cc' + page_url_soup[1]['href']
    url = last_page_url