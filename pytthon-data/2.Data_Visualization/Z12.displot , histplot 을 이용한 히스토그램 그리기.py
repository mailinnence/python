'''
참조
https://dining-developer.tistory.com/30
'''





'''
옵션 kde
kde = True (선을 보여줌)
kde = False (선을 보여줌)
defalut 값은 함수마다 다름

ex)
sns.histplot(df['sepal_length'], bins = 20, kde = True)

'''

# distplot ---------------------------------------------------------------
# distplot(df['칼럼명']) 칼럼 기준 그래프를 보여줌
# 데이터를 바로 받아서 출력해주는 그래프 
# 자체적으로 구간을 나눠서 보여줘서 편리하다는 장점이 있다.


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(rc={'figure.figsize':(10, 5)})
df = sns.load_dataset('iris')

print(df.head())


'''
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa

'''

sns.distplot(df['sepal_length'])
plt.show()

# 구간 개수 설정
sns.distplot(df['sepal_length'], bins = 15)
plt.show()

# -------------------------------------------------------------------------







# histplot ---------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(rc={'figure.figsize':(10, 5)})
df = sns.load_dataset('iris')

print(df.head(20))


'''
    sepal_length  sepal_width  petal_length  petal_width species
0            5.1          3.5           1.4          0.2  setosa
1            4.9          3.0           1.4          0.2  setosa
2            4.7          3.2           1.3          0.2  setosa
3            4.6          3.1           1.5          0.2  setosa
4            5.0          3.6           1.4          0.2  setosa
5            5.4          3.9           1.7          0.4  setosa
6            4.6          3.4           1.4          0.3  setosa
7            5.0          3.4           1.5          0.2  setosa
8            4.4          2.9           1.4          0.2  setosa
9            4.9          3.1           1.5          0.1  setosa
10           5.4          3.7           1.5          0.2  setosa
11           4.8          3.4           1.6          0.2  setosa
12           4.8          3.0           1.4          0.1  setosa
13           4.3          3.0           1.1          0.1  setosa
14           5.8          4.0           1.2          0.2  setosa
15           5.7          4.4           1.5          0.4  setosa
16           5.4          3.9           1.3          0.4  setosa
17           5.1          3.5           1.4          0.3  setosa
18           5.7          3.8           1.7          0.3  setosa
19           5.1          3.8           1.5          0.3  setosa

'''

sns.histplot(df['sepal_length'])
plt.show()

# 구간 개수 설정
sns.histplot(df['sepal_length'], bins = 20)
plt.show()

# count -> density
# stat` must be one of ['count', 'frequency', 'density', 'probability', 'proportion', 'percent']
sns.histplot(df['sepal_length'], bins = 20, kde = True, stat = 'density')
plt.show()



# -------------------------------------------------------------------------





# histplot ---------------------------------------------------------------
# 카테고리 별 분류 ------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(rc={'figure.figsize':(10, 5)})
df = sns.load_dataset('iris')

print(df.head(20))


#sns.histplot(df['sepal_length'], bins = 20, kde = True, stat = 'density', hue = 'species')
'''
이렇게 만들면 오류난다.
'''
sns.histplot(data = df, x = 'sepal_length', bins = 20, kde = True, stat = 'density', hue = 'species')
plt.show()

# x 축, y 축 변경
sns.histplot(data = df, y = 'sepal_length', bins = 20, kde = True, stat = 'density', hue = 'species')
plt.show()




# -------------------------------------------------------------------------





# histplot -------------------------------------------------------------
#차원 추가 - 농도를 통계 낼때 사용함 ------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(rc={'figure.figsize':(10, 5)})
df = sns.load_dataset('iris')

print(df.head(20))
sns.histplot(data = df, y = 'sepal_length', x = 'sepal_width')
plt.show()


# 칼라바 추가
sns.histplot(data = df, y = 'sepal_length', x = 'sepal_width', cbar = True)
plt.show()

# -------------------------------------------------------------------------









# displot -------------------------------------------------------------
# distplot 보다 상대적으로 정확하게 나눔 
 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(rc={'figure.figsize':(10, 5)})
df = sns.load_dataset('iris')

print(df.head(20))

# 방법.1
sns.displot(df['sepal_length'])
plt.show()

# 방법.2
sns.displot(data = df, x = 'sepal_length')
plt.show()

# 그림 크기 변경	 height = 높이, aspect = 넓이
sns.displot(data = df, x = 'sepal_length', height = 5, aspect = 3)
plt.show()

# histgram 과 한 옵션 사용(1)
a = sns.displot(data = df, y = 'sepal_length', bins = 20, kde = True, stat = 'density', hue = 'species')
plt.show()

# histgram 과 한 옵션 사용(2)
sns.displot(data = df, y = 'sepal_length', x = 'sepal_width', cbar = True)
plt.show()




# -------------------------------------------------------------------------









# jointplot -------------------------------------------------------------
# 점과 그래프 를 같이

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(rc={'figure.figsize':(10, 5)})
df = sns.load_dataset('iris')

print(df.head(20))

sns.jointplot(data = df,  x = 'sepal_width', y = 'sepal_length')
plt.show()


# -----------------------------------------------------------
# kind 의 설정을 바꾸면 출력을 바꿀 수 있다.
# -----------------------------------------------------------

# histplot 의 형식으로 변경
sns.jointplot(data = df,  x = 'sepal_width', y = 'sepal_length', kind = 'hist', cbar = True)
plt.show()


#그림 크기 변경(정사각형의 형태)
sns.jointplot(data = df,  x = 'sepal_width', y = 'sepal_length', kind = 'hist', cbar = True, height = 10)
plt.show()



# -------------------------------------------------------------------------


