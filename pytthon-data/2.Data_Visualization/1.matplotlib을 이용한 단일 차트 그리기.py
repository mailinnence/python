

# x 가 1, 2, 3 이고 y 가 4, 5, 6 인 그래프를 그리시오.----------------
import matplotlib.pyplot as plt


x = [1, 2, 3]
y = [4, 5, 6]

plt.figure()	# 변수명.figure()	>>  변수명으로 형태를 잡음
plt.plot(x, y)	# 가로행 세로열
plt.show()


# -------------------------------------------------------------------------






# lineplot 은 y 값만 있으면 그림을 그릴 수 있음--------------------

import matplotlib.pyplot as plt


x = [1, 2, 3]
y = [4, 5, 6]

plt.figure()	# 변수명.figure()	>>  변수명으로 형태를 잡음
plt.plot(y)		#  이 때, x 의 값은 0, 1, 2... 순서로 자동 지정됨
plt.show()



# -------------------------------------------------------------------------







# 옵션.1 -----------------------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]

plt.figure()	# 변수명.figure()	>>  변수명으로 형태를 잡음



# linewidth 를 이용한 선 굵기 조정
plt.plot(x, y, linewidth = 10)
plt.show()


# color 를 통한 선 색상 조정
plt.plot(x, y, color = 'red')
plt.show()


# marker 를 이용한 데이터 위치 표시
plt.plot(x, y, marker = 'o')
plt.show()

# marker 크기 변경
plt.plot(x, y, marker = 'o', markersize = 10)
plt.show()

# 점으로 표현된다.
plt.plot(x, y , 'bo')
plt.show()

# 붉은 점으로 표현된다.
plt.plot(x, y , 'ro')
plt.show()

# 붉은 선으로 표현된다.
plt.plot(x, y , 'r-')
plt.show()

#검은 점선으로 표현된다.
plt.plot(x, y , 'k--')
plt.show()

# 점선
plt.plot(x, y, linestyle = ':')
plt.show()

# 점
plt.plot(x, y, 'o')
plt.show()


# 붉은 점
plt.plot(x, y, 'ro')
plt.show()




# -------------------------------------------------------------------------











# 옵션2.-----------------------------------------------------------------

# 그래프 명
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]

plt.figure()	
plt.plot(x, y)
plt.title('title')
plt.show()


# 그래프 명 폰트 크기 변경
plt.plot(x, y)
plt.title('title', fontsize = 20)
plt.show()


# x 축 명, y 축 명
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 축 명 폰트 크기 변경
plt.plot(x, y)
plt.xlabel('x', fontsize = 20)
plt.ylabel('y', fontsize = 20)
plt.show()

# 그리드 설정(전체)
plt.plot(x, y)
plt.grid(True)
plt.show()

# 그리드 설정
plt.plot(x, y)
plt.grid(True, axis = 'x')
plt.show()

plt.plot(x, y)
plt.grid(True, axis = 'y')
plt.show()

# x 범위, y 범위 설정
plt.plot(x, y)
plt.xlim([1, 2])
plt.ylim([4, 5])
plt.show()


# axis 를 사용한 범위 설정
plt.plot(x, y)
plt.axis([1, 2, 4, 5])
plt.show()

# 눈금 글꼴 크기 변경
plt.plot(x, y)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 20)
plt.show()

# 그래프에 텍스트 삽입
plt.plot(x, y)
plt.text(2, 5, 'text', fontsize = '20')  	# ( 위치 , '텍스트' , fontsize )
plt.show()

# 한글폰트 사용하기
# 아래 코드를 실행하고, 런타임 -> 런타임 다시 시작 실행
'''
!pip install matplotlib -U
!sudo apt-get install -y fonts-nanum 
!sudo fc-cache -fv 
!rm ~/.cache/matplotlib -rf
'''
plt.plot(x)
plt.title('차트 명')
plt.show()





# -------------------------------------------------------------------------




]
