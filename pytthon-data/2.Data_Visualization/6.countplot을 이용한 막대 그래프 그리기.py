
# titanic 데이터 셋의 성별 인원수를 시각화 하시오.-----------------

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10, 5)})
import pandas as pd

df = sns.load_dataset('titanic')
a=df.groupby(by = 'sex')['sex'].count()
print(a)

 
# -------------------------------------------------------------------------


# 위의 것을 간단히 표현
# countplot 을 사용한 해결 -------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10, 5)})
import pandas as pd

df = sns.load_dataset('titanic')
a=df.groupby(by = 'sex')['sex'].count()

sns.countplot(data = df, x = 'sex')
plt.show()





# 가로로 그리기
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10, 5)})
import pandas as pd

df = sns.load_dataset('titanic')
a=df.groupby(by = 'sex')['sex'].count()

sns.countplot(data = df, y = 'sex')
plt.show()

# -------------------------------------------------------------------------



# 분류 안에서 나누기 ----------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10, 5)})
import pandas as pd

df = sns.load_dataset('titanic')
a=df.groupby(by = ['sex', 'class'])['sex'].count()
print(a)

sns.countplot(data = df, x = 'sex', hue = 'class')
#hue 는 새로운 변수를 다른 색상을 이용하여 추가하는 파라미터
plt.show()




#palette 를 사용한 색상 조정

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(10, 5)})
import pandas as pd

df = sns.load_dataset('titanic')
a=df.groupby(by = ['sex', 'class'])['sex'].count()
print(a)

sns.countplot(data = df, x = 'sex', hue = 'class', palette = 'flare')
plt.show()


# -------------------------------------------------------------------------
