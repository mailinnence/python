요약 튤을 사용해보자!



!pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip


import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
import seaborn as sns
df = sns.load_dataset('iris')


print(df.head(),'\n')
profile = ProfileReport(df)
profile.to_notebook_iframe()





데이터가 어떻게 결집해지는 것(EDA)을 좀 더 쉽게 그려주는 오픈 툴이
andas-profiling 이다!


import numpy as np
import pandas as pd
import seaborn as sns

# 가져오고
from pandas_profiling import ProfileReport

# 데이터를 가져오고
df = sns.load_dataset('iris')

# 이렇게 보던걸
print(df.head(),'\n')

# 데이터를 넣고
profile = ProfileReport(df)

# 출력해보면 좀 더 예쁘게 볼 수 있다.
profile.to_notebook_iframe()





