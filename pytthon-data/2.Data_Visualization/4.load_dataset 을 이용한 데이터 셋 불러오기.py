

# load_dataset ---------------------------------------------------------
# load_dataset 사용법. : sns.load_dataset('데이터 셋 이름')


import matplotlib.pyplot as plt 
# seaborn  >>  공부용으로 주는 데이터 셋  >>  pip install seaborn
import seaborn as sns
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

plt.scatter(df['petal_length'], df['petal_width'])
plt.show()

# -------------------------------------------------------------------------






# iris 데이터 셋의 petal_length 와 petal_width 를 이용하여 산점도를 그리시오.
#  seaborn으로 출력해보자

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

df = sns.load_dataset('iris')
print(df.head(),'\n')

plt.scatter(df['petal_length'], df['petal_width'])
sns.scatterplot(data = df, x = 'petal_length', y = 'petal_width')
plt.show()



# -------------------------------------------------------------------------








# matplotlib 과 호환-----------------------------------------------------




import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

df = sns.load_dataset('iris')
print(df.head(),'\n')

plt.scatter(df['petal_length'], df['petal_width'])
sns.scatterplot(data = df, x = 'petal_length', y = 'petal_width')
plt.title('iris')
plt.show()

# -------------------------------------------------------------------------



