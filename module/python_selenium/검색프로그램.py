
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())


print("검색할 내용을 입력하여라")
A=input()

#네이버 검색
driver.get('https://www.naver.com/')
Search= driver.find_element_by_name('query')
Search.send_keys(A)                                                               
Search.submit()
