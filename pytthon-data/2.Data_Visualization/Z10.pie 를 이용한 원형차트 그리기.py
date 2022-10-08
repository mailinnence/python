
#  원형차트 그리기 -------------------------------------------------
# pie(판다스['칼럼'])

import matplotlib.pyplot as plt
import pandas as pd

movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)
print(df)
 
'''
  	movie       aud
0   	  A  	 664308
1    	  B  	2099131
2     	  C   	 20067
'''



# plt.pie(df['movie'])
plt.pie(df['aud'], labels = df['movie']);	# 각 칼럼에 라벨 붙이기
plt.show()

# -------------------------------------------------------------------------









# 값 추가  -------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)
print(df)
 
'''
  	movie       aud
0   	  A  	 664308
1    	  B  	2099131
2     	  C   	 20067
'''


plt.pie(df['aud'], labels = df['movie'], autopct = '%0.2f%%');

# autopct: 파이 조각의 전체 대비 백분율.
'''
slice: 파이 차트를 구성할 데이터
labels: 파이 조각의 라벨
startangle: 그려지는 파이 조각 시작 위치. 90이면 12시 방향임. 파이 조각은 이 각도를 기준을 반시계 방향으로 그려짐
shadow: 파이 차트의 그림자 효과 유무
explode: 파이 조각이 돌출되는 크기. 0이면 돌출되지 않음
autopct: 파이 조각의 전체 대비 백분율.
'''

plt.show()

# -------------------------------------------------------------------------











# colors 를 이용한 색상 변경하기 -----------------------------------

import matplotlib.pyplot as plt
import pandas as pd

movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)
print(df)

#colors_list = ['red', 'green', 'blue']
colors_list = ['#F08080', '#DCDCDC', '#FFF8DC']
plt.pie(df['aud'], labels = df['movie'], autopct = '%0.2f%%' , colors = colors_list);

plt.show()

# -------------------------------------------------------------------------






# explode 를 이용한 중심으로부터 그림 떼어내기 --------------

import matplotlib.pyplot as plt
import pandas as pd

movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)
print(df)

#colors_list = ['red', 'green', 'blue']
colors_list = ['#F08080', '#DCDCDC', '#FFF8DC']

explode_list = [0, 0.1, 0]	# 1인 칼럼을 띄어낸다.
plt.pie(df['aud'], labels = df['movie'], autopct = '%0.2f%%' , colors = colors_list , explode = explode_list);

plt.show()


# -------------------------------------------------------------------------









