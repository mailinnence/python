




# 막대그래프로 표현---------------------------------------------------

import matplotlib.pyplot as plt
plt.rcParams['font.family']=['NanumGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

import seaborn as sns
import pandas as pd


movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)

print(df)


'''
        	           영화제목   		  누적관객
0    	           크루엘라   		  664308
1  	극장판 귀멸의 칼날: 무한열차편 	  2099131
2            	학교 가는 길    		  20067
'''

sns.barplot(data = df, x = 'movie', y = 'aud')
plt.show()

# -------------------------------------------------------------------------





# 차트 크기 변경 -------------------------------------------------------

import matplotlib.pyplot as plt
plt.rcParams['font.family']=['NanumGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

import seaborn as sns
import pandas as pd


movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)

print(df)


'''
        	           영화제목   		  누적관객
0    	           크루엘라   		  664308
1  	극장판 귀멸의 칼날: 무한열차편 	  2099131
2            	학교 가는 길    		  20067
'''

sns.barplot(data = df, x = 'movie', y = 'aud')
plt.show()


# -------------------------------------------------------------------------









# 차트 크기 변경 -------------------------------------------------------

import matplotlib.pyplot as plt
plt.rcParams['font.family']=['NanumGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

import seaborn as sns
import pandas as pd


movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)

print(df)

sns.set(rc={'figure.figsize':(10, 5)})
sns.barplot(data = df, x = 'movie', y = 'aud')
plt.show()


# -------------------------------------------------------------------------






# 정렬 -------------------------------------------------------------------

# 오름차순 - 누적관객수 별로 그리기
import matplotlib.pyplot as plt
plt.rcParams['font.family']=['NanumGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

import seaborn as sns
import pandas as pd


movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)

print(df)

sns.set(rc={'figure.figsize':(10, 5)})
sns.barplot(data = df, x = 'movie', y = 'aud', order = df.sort_values('aud').movie)
plt.show()





# 내림차순 - ascending 을 이용한 내림차순 정렬
import matplotlib.pyplot as plt
plt.rcParams['font.family']=['NanumGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

import seaborn as sns
import pandas as pd


movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)

print(df)

sns.set(rc={'figure.figsize':(10, 5)})
sns.barplot(data = df, x = 'movie', y = 'aud', order = df.sort_values('aud' , ascending = False ).movie)
plt.show()


# -------------------------------------------------------------------------













# 관객 수 포맷 변환----------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import pandas as pd

plt.rcParams['font.family']=['NanumGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False



movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)

print(df)
sns.set(rc={'figure.figsize':(10, 5)})

#경고문 제거
ticks_labels = chart.get_yticks().tolist()
chart.yaxis.set_major_locator(mticker.FixedLocator(ticks_labels))

chart = sns.barplot(data = df, x = 'movie', y = 'aud', order = df.sort_values('aud' , ascending = False ).movie)
ylabels = ['{:,.0f}'.format(i) + '만 명' for i in chart.get_yticks() / 10000]

chart.set_yticklabels(ylabels)
plt.show()


# -------------------------------------------------------------------------











# 가로로 그리기 -------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import pandas as pd

movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)

sns.set(rc={'figure.figsize':(10, 5)})

chart = sns.barplot(data = df, x = 'aud', y = 'movie', order = df.sort_values('aud' , ascending = False ).movie)
xlabels = ['{:,.0f}'.format(i) + 's' for i in chart.get_xticks() / 10000]
chart.set_xticklabels(xlabels)

plt.show()


# -------------------------------------------------------------------------








# 차트 색상 변경-----------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import pandas as pd

movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)

sns.set(rc={'figure.figsize':(10, 5)})

chart = sns.barplot(data = df, x = 'aud', y = 'movie', order = df.sort_values('aud' , ascending = False).movie ,color='blue')
xlabels = ['{:,.0f}'.format(i) + 's' for i in chart.get_xticks() / 10000]
chart.set_xticklabels(xlabels)

plt.show()

# -------------------------------------------------------------------------









# 제목 추가, 폰트 사이즈 변경 ----------------------------------------

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import pandas as pd

movie_title = ['A', 'B', 'C']
audience = [664308, 2099131, 20067]

data = {'movie' : movie_title, 'aud' : audience}
df = pd.DataFrame(data)

sns.set(rc={'figure.figsize':(10, 5)})

chart = sns.barplot(data = df, x = 'aud', y = 'movie', order = df.sort_values('aud' , ascending = False).movie ,color='blue')
xlabels = ['{:,.0f}'.format(i) + 's' for i in chart.get_xticks() / 10000]
chart.set_xticklabels(xlabels)

plt.xlabel('aud', fontsize = 15)
plt.ylabel('moive', fontsize = 15)
plt.title('wow', fontsize = 20)
plt.show()


# -------------------------------------------------------------------------





