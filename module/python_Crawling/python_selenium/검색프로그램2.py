#검색 프로그램 
#2021년 2월 12일 기준

print("검색할 내용을 입력하여라")
A=input()

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

#네이버 검색
driver.get('https://www.naver.com/')
Search= driver.find_element_by_name('query')
Search.send_keys(A)                                                               
Search.submit()

#네이버 이미지 검색
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://search.naver.com/search.naver?where=image&sm=tab_jum&query=')
Search= driver.find_element_by_name('query')
Search.send_keys(A)                                                                  
Search.submit()

#구글 검색
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.co.kr/')
Search = driver.find_element_by_name('q')
Search.send_keys(A)                                                                 
Search.submit()

#구글이미지 검색
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl')
Search= driver.find_element_by_name('q')
Search.send_keys(A)                                                                  
Search.submit()
Search= driver.find_element_by_class_name("hide-focus-ring")
Search.click()   
Search= driver.find_element_by_class_name("rg_i.Q4LuWd")
Search.click() 


