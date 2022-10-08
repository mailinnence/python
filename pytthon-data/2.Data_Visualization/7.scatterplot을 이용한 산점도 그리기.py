
# iris 데이터 셋을 이용하여 sepal_length, sepal_width 별 산점도를 작성하시오.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('iris')		# 데이터 가져오기
df.head()
sns.set(rc={'figure.figsize':(10, 5)}) 	# 크기 정하고
sns.scatterplot(data = df, x = 'sepal_width', y = 'sepal_length') 
plt.show()

# -------------------------------------------------------------------------






# hue 를 이용한 종 분류

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('iris')		# 데이터 가져오기
df.head()
sns.set(rc={'figure.figsize':(10, 5)}) 	# 크기 정하고
sns.scatterplot(data = df, x = 'sepal_width', y = 'sepal_length', hue = 'species')
plt.show()
# -------------------------------------------------------------------------









#  petal_length 의 값을 3 미만, 5 미만, 5 이상으로 분류하여 표시하여라.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def function1(x):
    if x < 3:
        return 's'
    elif x < 5:
        return 'm'
    else:
        return 'l'



df = sns.load_dataset('iris')		# 데이터 가져오기
df.head()
sns.set(rc={'figure.figsize':(10, 5)}) 	# 크기 정하고
df['petal_length2'] = df['petal_length'].apply(function1)	# 함수 적용시기코
sns.scatterplot(data = df, x = 'sepal_width', y = 'sepal_length', hue = 'species',
 style = 'petal_length2')
# 행열 구분류하고 >> 색깔 분류하고(species)  >> 모양으로 분류(petal_length2)

print(df)
plt.show()

# -------------------------------------------------------------------------








# relplot 을 이용하면 카테고리 별로 따로 그릴 수 있음


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def function1(x):
    if x < 3:
        return 's'
    elif x < 5:
        return 'm'
    else:
        return 'l'



df = sns.load_dataset('iris')		# 데이터 가져오기
df.head()
sns.set(rc={'figure.figsize':(10, 5)}) 	# 크기 정하고
df['petal_length2'] = df['petal_length'].apply(function1)	# 함수 적용시기코
sns.relplot(data = df, x = 'sepal_width', y = 'sepal_length', col = 'species')
# col 무엇을 기준으로 하나씩 줄 것인가?

print(df)
plt.show()

# -------------------------------------------------------------------------








# lmplot 을 사용하면 회귀선을 그릴 수 있음

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def function1(x):
    if x < 3:
        return 's'
    elif x < 5:
        return 'm'
    else:
        return 'l'



df = sns.load_dataset('iris')		# 데이터 가져오기
df.head()
sns.set(rc={'figure.figsize':(10, 5)}) 	# 크기 정하고
df['petal_length2'] = df['petal_length'].apply(function1)	# 함수 적용시기코
sns.lmplot(data = df, x = 'sepal_width', y = 'sepal_length', hue = 'species')

print(df)
plt.show()

# -------------------------------------------------------------------------


