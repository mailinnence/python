#1.request 응답 상태

import requests        #HTTP 요청을 보내는 모듈
#https://www.daleseo.com/python-requests/ 참조
#https://dgkim5360.tistory.com/entry/python-requests
#print(dir(requests)) #dir() 내장 함수는 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메소드(method)를 가지고 있는지 나열해줍니다.

url="https://www.naver.com/"
print(requests.post(url))
print(requests.post(url))
print(requests.post(url))
response=requests.get(url)
#<Response [200]> 즉 요청이 잘됬다
print(response.status_code) #요청의 숫자가 나온다

#######################################################
#<Response [200]> 요청이 잘됬다
#<Response [404]> 요청이 안됬다
#<Response [201]>
#먼저 코딩으로 값을 주어 웹의 반응을 알아보여면 requests 모듈을 알아봐야 한다
#requests 는 HTTP 요청을 보내는 모듈로



def main():
    #print(dir(requests)) 모듈안에 메소드나 변수가 뭐 있는지 알아보는 함수
    url="https://www.naver.com/"
    requests.post(url)     #살아있는지 확인하는 코드
    print(requests.post(url))   #post 방식으로 살아있는지 확인하는 코드
    print(requests.get(url))    #get 방식으로 살아있는지 확인하는 코드
    
    
if __name__=='__main__':
        main()
