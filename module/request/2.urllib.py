import urllib  # URL 작업을 위한 여러 모듈을 모은 패키지입니다
import urllib.parse   # URL을 구성 요소로 구문 분석
import urllib.request #url의 반응을 살피는 모듈
import requests #HTTP 요청을 보내는 모듈

def get(url):
    import urllib.request
    response=urllib.request.urlopen(url)
    data=response.read()
    decoded=data.decode("utf-8")
    return decoded

url="https://www.naver.com/"
content=get(url)
print(content)


response = requests.post("https://www.naver.com/")
print(response.text)    # UTF-8로 인코딩된 문자열을 얻을 수 있다.
print(response.headers) # headers 속성을 통해 사전의 형태로 얻을 수 있다
print(response.headers['Content-Type']) # headers의 문서종류를 출력해줌

print(requests.post("http://localhost/3.dvwa/1.brutefource/1-3.bruteforce-GET.php", params={'name': 'Test User'}))


