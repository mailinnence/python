#유용한 코딩

'''
input = sys.stdin.readline()은 표준 입력에서 한 줄을 읽어와 input 변수에 할당하는 것을 의미합니다. 
이를 통해 표준 입력을 더욱 빠르게 처리할 수 있습니다. 이 방법은 입력이 많은 경우 일반적인 input() 함수보다 빠르게 동작합니다.
'''


# 반올림
f, g, h = 3.159, 6.23791, 11.2795801
print("%.2f, %.2f, %.2f" % (round(f, 2), round(g, 2), round(h, 2)))

>> 3.16, 6.24, 11.28


#리스트 한번에 넣기
# a=list(map(int , input().split()))


# 2중 리스트 받기
 mylist = [list(input()) for _ in range(8)]

# 2차 행렬 반전 뒤집기
mylist2 = list(map(list, (zip(*mylist))))

# 리스트레 inpput
>>> li=list([input()])
a a a a a
>>> li
['a a a a a']


# 범위 조건
text="abcde"
if "d" in text[2:]: print("exist")
   
   
   

#변수 한번에 넣기
a,b=map(int , input().split())


# 리스트를 입력처럼 보여줌
list=[1,2,3,4,5]
print(*list)

>>> 1 2 3 4 5




#문자열에 변수넣는 방법
print(f"#{test_case} {most}")






#리스트 여러개 만들기
a=[[0] * s for i in range(s)]

numbers = [ ] 
for n in range(1, 100+1):
    numbers.append(n) 

#와
numbers = [ x for x in range(1, 101)]

#는 같다

#리스트 인덱스만 출력하는 방법
#ex.0)-----------------------------------------------------------------------------------------
a=[1,2,3,4,5]
print(*a)
-----------------------------------------------------------------------------------------------

#ex.1)-----------------------------------------------------------------------------------------
for i in a:
    print(*[x for x in i if x !=0]) 
-----------------------------------------------------------------------------------------------

#ex.2)-----------------------------------------------------------------------------------------
x=3
a=[3 * x for i in range(3)]
print(a)

#>>[9, 9, 9]    
-----------------------------------------------------------------------------------------------


#ex.3)-----------------------------------------------------------------------------------------
x=3
a=[int(input())  for i in range(3)]
#3
#5
#7
print(a)

#>>[3, 5, 7]
-----------------------------------------------------------------------------------------------


#ex.4)-----------------------------------------------------------------------------------------
x=list(map(int , input().split()))
a=[list(map(int , input().split()))  for i in range(3)]
#1 1 1 1 1
#2 2 2 2 2
#3 3 3 3 3
print(a)
#[[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]
-----------------------------------------------------------------------------------------------





#역문자
s="abcdefg"
re_s=s[::-1]






# 리스트 모든 원소 출력 시 한 줄에 출력 시간관리법
n = int(input())
li = [] 

for i in range(n):
    num = int(input())
    li.append(num)

print(' '.join(map(str, li)))
'''
위 코드에서 join() 함수는 리스트의 모든 값을 문자열로 변환한 후, 공백을 구분자로 
사용하여 이어붙인 문자열을 반환합니다. map(str, li)는 리스트 li의 모든 값을 문자열로 변환한 이터레이터를 반환하고, 
' '.join(...)은 이 이터레이터를 공백으로 구분하여 이어붙인 문자열을 반환합니다.
'''





#모든 경우의 수를 만들기
import itertools
from itertools import permutations

#ex).1 반복문으로 만들기
for i in permutations("123",3):
    print(i)    
    
# ('1', '2', '3')
# ('1', '3', '2')
# ('2', '1', '3')
# ('2', '3', '1')
# ('3', '1', '2')
# ('3', '2', '1')

#ex).2 리스트로 만들기
import itertools
pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
    
    
    
    
    
    
#문자열 사이에 변수 쓰기
# 다음 주어진 변수를 활용하여 문제3의 코드를 작성하세요.
epoch = 10
train_accuracy = 0.85; val_accuracy = 0.83; test_accuracy = 0.76
model_name = "ResNet44"


# 가능하면 배웠던 3가지 케이스를 모두 사용해보세요;.
# case1 %
print("{} 모델로 {} epoch를 돌려 학습시킨 결과는 학습 정확도 : {}, 검증 정확도 : {}, 테스트 정확도 : {}으로 나왔습니다".format("ResNet44", 10, 0.85, 0.83, 0.76))
# case2
print("%s 모델로 %d epoch를 돌려 학습시킨 결과는 학습 정확도 : %.2f, 검증 정확도 : %.2f, 테스트 정확도 : %.2f으로 나왔습니다" % ("ResNet44", 10, 0.85, 0.83, 0.76))
# case3
print(f"{model_name} 모델로 {epoch} epoch를 돌려 학습시킨 결과는 학습 정확도 : {train_accuracy}, 검증 정확도 : {val_accuracy}, 테스트 정확도 : {test_accuracy}으로 나왔습니다")
    
 '''
ResNet44 모델로 10 epoch를 돌려 학습시킨 결과는 학습 정확도 : 0.85, 검증 정확도 : 0.83, 테스트 정확도 : 0.76으로 나왔습니다
ResNet44 모델로 10 epoch를 돌려 학습시킨 결과는 학습 정확도 : 0.85, 검증 정확도 : 0.83, 테스트 정확도 : 0.76으로 나왔습니다
ResNet44 모델로 10 epoch를 돌려 학습시킨 결과는 학습 정확도 : 0.85, 검증 정확도 : 0.83, 테스트 정확도 : 0.76으로 나왔습니다
''' 



#lamda
## (정답)

## 1) pythagoras 함수를 lambda 함수로 구현한 pythagoras_lambda() 입니다. 
pythagoras_lambda = lambda num1, num2 : (num1**2 + num2**2)**0.5

## 2) 숫자 3, 4를 pythagoras_lambda()에 넣고 실행합니다.
pythagoras_lambda(3, 4)





#함수 조건식
def height_high(height):  
    return '키가 정말 크군요' if height >= 180 else '계속 클 것 입니다. : )'
  
print(height_high(181))    





#다량의 변수를 함수식에 넣고 싶을때
## (정답)

## 1) height_high 함수를 다음과 같인 선언합니다. 
def height_high(height):  
    return '키가 정말 크군요' if height >= 180 else '계속 클 것 입니다. : '
  
print(height_high(181))    


dict_heights = {'rohoon_height' : 178, 'yongdam_height': 180, 'sungwoong_height' : 175, 'youngmin_height' : 176, 'Gwangsoo_height': 180}

print(list(map(height_high, dict_heights.values())))

>>
키가 정말 크군요
['계속 클 것 입니다. : ', '키가 정말 크군요', '계속 클 것 입니다. : ', '계속 클 것 입니다. : ', '키가 정말 크군요']
>>






#filter 함수
dict_heights = {'rohoon_height' : 178, 'yongdam_height': 180, 'sungwoong_height' : 175, 'youngmin_height' : 176, 'Gwangsoo_height': 180}

print(list(filter(lambda name : True if dict_heights[name] >= 180 else False, dict_heights)))




#딕션너리
- iter() 함수로 반복 가능한 객체를 생성합니다. 
- next() 함수로 반복 가능한 객체의 원소를 하나씩 반환하도록 합니다.
- next() 함수를 총 세 번을 실행하고, 각 실행시의 출력결과를 살펴보세요.


dict_heights = {'rohoon_height' : 178, 'yongdam_height': 180, 'sungwoong_height' : 175, 'youngmin_height' : 176, 'Gwangsoo_height': 180}
height_iter = iter(dict_heights)

print(next(height_iter))
print(next(height_iter))
print(next(height_iter))
print(next(height_iter))

>>>
rohoon_height
yongdam_height
sungwoong_height
youngmin_height
>>>









#데코레이터 함수 만들기
---------------------------------------------
def hello():
    print('hello 함수 시작')
    print('hello')
    print('hello 함수 끝')
 
def world():
    print('world 함수 시작')
    print('world')
    print('world 함수 끝')
 
hello()
world()



>>>
hello 함수 시작
hello
hello 함수 끝
world 함수 시작
world
world 함수 끝
>>>
---------------------------------------------

'''
번거롭다!
아래부터는 이를 데코레이터 함수를 이용하려 좀 더 간단하게 표현해보자
'''

---------------------------------------------
def 함수명(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():                            # trace 함수 안에서는 호출할 함수를 감싸는 함수 wrapper를 만든다. (호출할 함수를 감싸는 함수)
        func()                                
    return wrapper                            

def 함수1():
    print(3333)

    
    
>>>
3333
>>>
---------------------------------------------
    
    
---------------------------------------------    
def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():                           # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')      # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
 
def hello():
    print('1번 함수')
 
def world():
    print('2번 함수')



>>>
hello 함수 시작
1번 함수
hello 함수 끝
world 함수 시작
2번 함수
world 함수 끝
>>>

---------------------------------------------


더 간결히!

---------------------------------------------
def trace(func):  
    def wrapper():
        func()    
    return wrapper  
 
@trace    # @데코레이터
def hello():
    print('1번 함수')
 
@trace    # @데코레이터
def world():
    print('2번 함수')
 
hello()    # 함수를 그대로 호출
world()    # 함수를 그대로 호출
---------------------------------------------


---------------------------------------------
import random

def do_you_know_password(func):
    def wrapper(*args, **kwargs):
        right_password = 'python38'
        passwords = input("비밀번호를 입력하세요: ")
        if passwords == right_password:
            result = func(*args, **kwargs)
        else:
            result = '입력하신 비밀번호는 올바른 비밀번호가 아닙니다.'
        return result
    return wrapper


@do_you_know_password
def lotto_generator():
    lotto_numbers=[]
    lotto_numbers_for = []
    for count in range(6):
        lotto_num = random.randint(1, 45)
        if lotto_num not in lotto_numbers:
            lotto_numbers_for.append(lotto_num)

    lotto_numbers_for.sort()
    
    return lotto_numbers_for

## 03 함수 실행!
print(lotto_generator())

---------------------------------------------


격자 방식
---------------------------------------------

    for i in range(N):
        for j in range(M):
            if (i+j) % 2 == 0:
                boardA.append(board[i][j])
            if (i+j) % 2 == 1:
                boardB.append(board[i][j])
     
---------------------------------------------





# 리스트로 도형     
---------------------------------------------
def draw_stars(n):
    if n==1:
        return ['*']

    Stars=draw_stars(n//3)
    L=[]

    for star in Stars:
        L.append(star*3)
    for star in Stars:
        L.append(star+' '*(n//3)+star)
    for star in Stars:
        L.append(star*3)

    return L

N=int(input())
print('\n'.join(draw_stars(N)))     
---------------------------------------------
