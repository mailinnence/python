
# 선도표 그리기

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('flights')
sns.set(rc={'figure.figsize':(10, 5)})
sns.lineplot(data = df, x = 'year', y = 'passengers')

plt.show()

# -------------------------------------------------------------------------






# xtick 에 전체 년도 표시

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('flights')
sns.set(rc={'figure.figsize':(10, 5)})
sns.lineplot(data = df, x = 'year', y = 'passengers')

# 각 옵션들을 넣을 수 있다.
plt.xticks(df['year'], rotation = 45);


plt.show()

# -------------------------------------------------------------------------






# xtick 기울기 추가

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('flights')
sns.set(rc={'figure.figsize':(10, 5)})
sns.lineplot(data = df, x = 'year', y = 'passengers')
plt.xticks(df['year']);

plt.show()

# -------------------------------------------------------------------------





# 월별로 그리기

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('flights')
sns.set(rc={'figure.figsize':(10, 5)})
sns.lineplot(data = df, x = 'year', y = 'passengers', hue = 'month')
sns.lineplot(data = df, x = 'year', y = 'passengers', hue = 'month', palette = 'Set2', style = 'month')
# hue 는 새로운 변수를 다른 색상을 이용하여 추가하는 파라미터
# 색상 , 선 스타일 선택 가능
plt.xticks(df['year']);

plt.show()

# -------------------------------------------------------------------------




