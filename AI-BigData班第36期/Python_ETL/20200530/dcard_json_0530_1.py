import requests
import json
from urllib.request import urlretrieve

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
url = 'https://www.dcard.tw/service/api/v2/forums/game/posts?limit=30&before=233743555'

# 因dcard是用get訪問，所以用get
res = requests.get(url=url,headers=headers)

# print(res.text) 發現回傳的是字串，所以不用beautifulsoup，而是用json
# 字串轉dict or list，看最外層是{}還是[]判斷。
json_data = json.loads(res.text)

# print(json_data[0])
# print(json_data[1])
# print(json_data[2])

# 以下是看json_data[0]裡面有哪些key值。
# for k in json_data[0]:
#     print(k)

# get title,id
for t in json_data:
    title_name = t['title']
    article_url = 'https://www.dcard.tw/f/funny/p/'+ str(t['id'])
    print(title_name)
    print(article_url)

    # get images url,用urllib被擋下來了，所以換用requests的了
    # image_url_list = [img['url'] for img in t['mediaMeta']]
    # print(image_url_list)
    # for image_url in image_url_list:
    #     urlretrieve(image_url,'./dcardimg/'+ image_url.split('/')[-1])

    # get images url,用requests
    image_url_list = [img['url'] for img in t['mediaMeta']]
    print(image_url_list)
    for image_url in image_url_list:
        res_img = requests.get(image_url,headers=headers)
        img_content = res_img.content
        try:
            with open('./dcardimg/' + image_url.split('/')[-1],'wb')as f:
                f.write(img_content)
        except OSError as e:
            print()