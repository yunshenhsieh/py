from selenium.webdriver import Chrome

driver = Chrome('./chromedriver')
url='https://www.ptt.cc/bbs/index.html'

driver.get(url)

driver.find_element_by_class_name('board-name').click()
driver.find_element_by_class_name('btn-big').click()

cookie = driver.get_cookies()
print(cookie)