import requests
from bs4 import BeautifulSoup
import pandas as pd

# keyin=input('請輸入關鍵字：')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url='https://www.104.com.tw/jobs/search/?keyword={}&order=2&jobsource=2018indexpoc&ro=0'.format('python')


company_data=[]
title_data=[]
href_data=[]

dict_tool={}
dict_skill={}
dict_tool_skill=[]

res = requests.get(url=url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
company_list=soup.select('a[title]')
title_list = soup.select('article[class]')
for element in company_list:
    try:
        company_data.append(element.text.strip())
    except:
        print('=========')
        print(company_data)
        print('=========')



for num in range(len(title_list)):
    try:
        good_tool = []
        total_skill = []
        title=title_list[num].select('a')
        href=title_list[num].select('a')[0]['href']
        title_data.append(title[0].text)

        # 下面這段要搭配docker上使用splash，但不知道為什麼，第1頁的第7個職缺，批次會抓不到「擅長工具」和「工作技能」，但是自己輸入就抓的到。
        # 教學網址：https://www.itread01.com/content/1578970986.html
        url_splash = 'http://localhost:8050/render.html?url=https://{}'.format(href[2:])
        res = requests.get(url_splash)
        soup = BeautifulSoup(res.text, 'html.parser')
        tool = soup.select('a[class="tools text-gray-deep-dark d-inline-block"]')
        skill = soup.select('a[class="skills text-gray-deep-dark d-inline-block"]')

        for tool in tool:
            good_tool.append(tool.text)
        for sk in skill:
            total_skill.append(sk.text)
        dict_tool[title[0].text+'擅長工具']=good_tool
        dict_skill[title[0].text+'工作技能']=total_skill


    except:
        print('==========')
        print(title)
        print('==========')

dict_tool_skill=[dict_tool,dict_skill]
txt=str(dict_tool_skill).replace('[{','{').replace('}]','}').replace('], ','],').replace(', {',',{')
txt=txt.split('},')

tool=txt[0].split('],')
tool=[i.replace('{','').replace('\'','').replace('[','').replace(']','').replace('}','').strip().split(':') for i in tool]
tool_df=[]
for i in range(len(tool)):
    tool[i][1]=tool[i][1].split(',')
for i in range(len(tool)):
    tool_df.append(str(tool[i][1]))

skill=txt[1].split('],')
skill=[i.replace('{','').replace('\'','').replace('[','').replace(']','').replace('}','').strip().split(':') for i in skill]
skill_df=[]
for i in range(len(skill)):
    skill[i][1]=skill[i][1].split(',')
for i in range(len(skill)):
    skill_df.append(str(skill[i][1]))
print(len(skill_df))
print(len(tool_df))
df=pd.DataFrame(columns=['公司名稱','職缺','擅長工具','工作技能'])
df['公司名稱']=company_data[2:]
df['職缺']=title_data
df['擅長工具']=tool_df
df['工作技能']=skill_df
df.to_csv('./hw_final.csv',index=0)