


# data1(x : 1, 2, 3; y : 1, 2, 3) 과 data2(x : 1, 2, 3; y : 1, 4, 7) 을 그래프로 출력하시오.------
# 두 개 이상은 이렇게 한다.
import matplotlib.pyplot as plt
x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 4, 7]

plt.plot(x1, y1, color = 'blue')
plt.plot(x2, y2, color = 'red')
plt.show()


# 한번에 이렇게 표현할 수 도 있다
plt.plot(x1, y1, 'b', x2, y2, 'r')
plt.show()

# -------------------------------------------------------------------------





# 라벨 사용 --------------------------------------------------------------
# data1(x : 1, 2, 3; y : 1, 2, 3) 과 data2(x : 1, 2, 3; y : 1, 4, 7) 을 그래프로 출력하시오.

import matplotlib.pyplot as plt
x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 4, 7]

# 라벨 사용.1
plt.plot(x1, y1, color = 'blue', label = 'data1')
plt.plot(x2, y2, color = 'red', label = 'data2')
plt.legend()
plt.show()

# 라벨 사용.2
plt.plot(x1, y1, color = 'blue')
plt.plot(x2, y2, color = 'red')
plt.legend(['data1', 'data2'])
plt.show()

# 라벨 사용.3 - 위치 설정
plt.plot(x1, y1, color = 'blue')
plt.plot(x2, y2, color = 'red')
plt.legend(['data1', 'data2'], loc = 'upper right')
plt.show()

'''
best		0
upper right	1
upper left	2
lower left		3
lower right	4
right		5
center left	6
center right	7
lower center	8
upper center	9
center		10
'''


# 라벨 사용.4 - 범례 폰트 사이즈 변경
plt.plot(x1, y1, color = 'blue')
plt.plot(x2, y2, color = 'red')
plt.legend(['data1', 'data2'], fontsize = 20)
plt.show()



# -------------------------------------------------------------------------





# data1(x : 1, 2, 3; y : 1, 2, 3) 과 data2(x : 1, 2, 3; y : 1, 100, 200) 을 그래프로 출력하시오.


import matplotlib.pyplot as plt
x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 100, 200]

plt.plot(x1, y1, color = 'blue')
plt.plot(x2, y2, color = 'red')
plt.show()



# -------------------------------------------------------------------------


