from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import selenium.webdriver


options=selenium.webdriver.ChromeOptions()
options.add_argument('--headless')
driver = selenium.webdriver.Chrome(chrome_options=options,executable_path='./chromedriver')
# 下面這行是會讓瀏覽器在前景執行，上面三行是讓瀏覽器在背景直接執行，選一個用就行了。
# driver = Chrome('./chromedriver')

url='https://www.104.com.tw/job/6wqvf?jobsource=hotjob_chr'

driver.get(url)

element = WebDriverWait(driver,5).until(expected_conditions.presence_of_element_located((By.ID,'app')))

soup = BeautifulSoup(driver.page_source,'html.parser')
print(soup)

driver.quit()