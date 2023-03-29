#3인스타 자동 좋아요 봇 기본 폼
#2021년 2월 19일 기준으로 원하는 사람 타임라인을 넣어주기만 하면 아주 잘 작동한다
# 4.에 원하는 주소와 8.에 원하는 횟수를 적어라 


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

#1.인스타 접속
driver.get('https://www.instagram.com/')
time.sleep(3)                                                                                  #로그인하는 사이에 코드가 진행 되기 때문에 잠깐 쉬어주어야 한다
  
#2.로그인
id = driver.find_element_by_name('username')
id.send_keys("mailinnence@gmail.com")

pw = driver.find_element_by_name('password')
pw.send_keys("dhkd2614!!")
pw.submit()
time.sleep(3)

#3.알림 설정 파괴
Search = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/button")                                          
Search.click()
time.sleep(3)
Search = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2] ')                                          
Search.click()



#4.원하는 사람 타임라인 으로 이동
driver.get('https://www.instagram.com/dlwlrma/')                                          #주소를 치면 된다
time.sleep(5)

#5.첫번째 게시물 선                                                                                                              #예시 아이유 인스타
xt=driver.find_element_by_xpath('//article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]')                              #주소를 찾아가 줘야 한다.....이게 좀 버거롭다...무슨말이냐면 /html/body/div[1]/section/main/div/div[4]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]    
xt.click()                                                                                                                            #위 의 주소를 줄인 것이 //article/div[1]/div/div[1]/div[1]/a/div[1]/div[2] 이기 때문이다
time.sleep(2)

#6.좋아요 버튼 클릭
good=driver.find_elements_by_xpath('//article//section/span/button')                 #주의 사항 elements 이다. 이유는 하나의 경로 주소에서 다수의 버튼 중 하나를 누르기 때문이다   위와 마찬가지로 주소를 좀 찾아 줘야한다 /html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg
good[0].click()                                                                                         #다수의 버튼 중 첫번째는 0이다 알다싶이 파이썬의 처음은 0부터 시작한다                                                                                     이것을 줄인 것이다. >>> //article//section/span/button 이렇게...
time.sleep(5)

#7.다음 게시물로 이동
time.sleep(5)
next=driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a ')     #css함수 사용 
next.click()
time.sleep(4)

#8.다음 게시물로 이동하는데 버튼이 두개라 오류가 난다... 그러므로 이를 방지하자...
#몇번 반복 할 것인지 설정
for i in range(10):
 good=driver.find_elements_by_xpath('//article//section/span/button')   #주의 사항 elements 이다. 이유는 하나의 경로 주소에서 다수의 버튼 중 하나를 누르기 때문이다
 good[0].click()                                                                           #다수의 버튼 중 첫번째는 0이다 알다싶이 파이썬의 처음은 0부터 시작한다
 time.sleep(4)
 next=driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
 next.click()
 time.sleep(4)



#여기까지 복사 갔다 붙여야 바로 실행


