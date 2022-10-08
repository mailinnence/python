
# boxplot 그리기 -----------------------------------------------------


import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10, 5)})
import pandas as pd


df = sns.load_dataset('iris')
print(df.head(),'\n')


'''
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa

'''


# 칼럼의 표본편차와 평균과 중간값등을 한 눈에 보여줌
sns.boxplot(data = df)
plt.show()

# -------------------------------------------------------------------------






# 세로방향으로 그림 크기 키우기 ---------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10, 5)})
import pandas as pd


df = sns.load_dataset('iris')
print(df.head(),'\n')

#사이즈 조정은 subplots 을 사용
plt.subplots(figsize = (7, 8))
sns.boxplot(data = df)
plt.show()

# -------------------------------------------------------------------------






# 가로 방향으로 그리기 -----------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10, 5)})
import pandas as pd


df = sns.load_dataset('iris')
print(df.head(),'\n')

# 사이즈 조정은 subplots 을 사용
plt.subplots(figsize = (7, 8))

# orient = 'h' 가로로 나오게 출력
'''
가로 horizontal 의 h
세로 horizontal 의 v (defalut)
'''
sns.boxplot(data = df, orient = 'h')
plt.show()

# -------------------------------------------------------------------------





# swarmplot -------------------------------------------------------------
# swarmplot 을 이용한 raw data 확인 (boxplot 과 다르게 정보가 가공되지 않음)


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(rc={'figure.figsize':(10, 5)})
df = sns.load_dataset('iris')
print(df.head(),'\n')

# 사이즈 조정은 subplots 을 사용

plt.subplots(figsize = (10, 10))
sns.swarmplot(data = df)

plt.show()

# -------------------------------------------------------------------------







# 겹쳐 그리기 -------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(rc={'figure.figsize':(10, 5)})
df = sns.load_dataset('iris')
print(df.head(),'\n')

plt.subplots(figsize = (10, 10))
sns.boxplot(data = df)
sns.swarmplot(data = df)
plt.show()

# -------------------------------------------------------------------------




# swarmplot 색상 조정 ----------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(rc={'figure.figsize':(10, 5)})
df = sns.load_dataset('iris')
print(df.head(),'\n')

plt.subplots(figsize = (10, 10))
sns.boxplot(data = df)
sns.swarmplot(data = df, color = 'black')

plt.show()

# -------------------------------------------------------------------------





# violinplot------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(rc={'figure.figsize':(10, 5)})
df = sns.load_dataset('iris')
print(df.head(),'\n')

sns.violinplot(data = df)
plt.show()

# -------------------------------------------------------------------------





# stripplot --------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(rc={'figure.figsize':(10, 5)})
df = sns.load_dataset('iris')
print(df.head(),'\n')

sns.stripplot(data = df)
plt.show()

# -------------------------------------------------------------------------




