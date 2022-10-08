

# 서로 다른 그래프를 그릴 때 사용
'''
 subplot을 이용한 해결 >> subplot(행의 수, 열의 수, 해당 그래프가 그려질 위치)
 data1(x : 1, 2, 3; y : 1, 2, 3) 과 data2(x : 1, 2, 3; y : 1, 100, 200) 을 그래프로 출력하시오.
'''

import matplotlib.pyplot as plt
x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 100, 200]

plt.subplot(1, 2, 1)
plt.plot(x1, y1)
plt.title('data1')

plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.title('data2')

plt.show()



plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.title('data1')

plt.subplot(2, 1, 2)
plt.plot(x2, y2)
plt.title('data2')
plt.show()



# -------------------------------------------------------------------------





# tight_layout 을 이용하면 레이아웃이 자동으로 설정됨 -----------

import matplotlib.pyplot as plt
x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 100, 200]

plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.title('data1')

plt.subplot(2, 1, 2)
plt.plot(x2, y2)
plt.title('data2')

plt.tight_layout()
plt.show()





# -------------------------------------------------------------------------




# subplots 사용------------------------------------------------------------

import matplotlib.pyplot as plt
x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 100, 200]

# fig 에 모형을 잡고 axe1 세부 설정을 한다.
# 행 nrows 열 ncols
fig, axe1 = plt.subplots(nrows = 1, ncols = 2)

axe1[0].plot(x1, y1, color = 'blue')
axe1[1].plot(x2, y2, color = 'red')
fig.show()

# -------------------------------------------------------------------------






# data1(x : 1, 2, 3; y : 1, 2, 3) 과 data2(x : 1, 2, 3; y : 1, 50, 200) 을 그래프로 출력하시오. ---------

import matplotlib.pyplot as plt
x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 50, 200]

fig, axe1 = plt.subplots()	#방향 : 남서

# 하나에 두개를 넣어줌 축을 전부 활용하여 그래프를 만든다.
axe2 = axe1.twinx()		#방향 :  북동 단 겹치면 겹치게 나옴
axe1.plot(x1, y1, color = 'red', label = 'data1')
axe2.plot(x2, y2, color = 'blue', label = 'data2')

axe1.set_xlabel('x', fontsize = 15)	# x의 라벨
axe1.set_ylabel('y1', fontsize = 15)	# y의 라벨
axe2.set_ylabel('y2', fontsize = 15)	# x의 라벨

fig.show()


# -------------------------------------------------------------------------







# y 축을 두 개 가진 차트에서 범례 표시하기 ------------------------

import matplotlib.pyplot as plt
x1 = [1, 2, 3]
y1 = [1, 2, 3]
x2 = [1, 2, 3]
y2 = [1, 50, 200]

fig, axe1 = plt.subplots()

axe2 = axe1.twinx()
chart1 = axe1.plot(x1, y1, color = 'red')
chart2 = axe2.plot(x2, y2, color = 'blue')

axe1.set_xlabel('x', fontsize = 15)
axe1.set_ylabel('y1', fontsize = 15)
axe2.set_ylabel('y2', fontsize = 15)

chart = chart1 + chart2
axe1.legend(chart, ['data1', 'data2'])

fig.show()

# -------------------------------------------------------------------------




