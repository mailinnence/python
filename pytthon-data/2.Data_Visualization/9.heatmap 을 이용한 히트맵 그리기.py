


# 데이터 형태 확인 ------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('flights')
sns.set(rc={'figure.figsize':(10, 5)})


print(df ,'\n')
print(df.head(10) ,'\n')



# -------------------------------------------------------------------------






# pivot 을 사용한 데이터 형태 변경 ------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('flights')
sns.set(rc={'figure.figsize':(10, 5)})

print(df ,'\n')
print(df.head(10) ,'\n')

# heatmap 에 사용할 수 있도록 데이터 형태 변경
pivot_data = df.pivot("month", "year", "passengers")

#sns.heatmap(pivot_data)
sns.heatmap(pivot_data, linewidths=.5)  # 구분선 추가
plt.show()




# cmap 을 통한 colorbar 색상 변경
sns.heatmap(pivot_data, cmap="Blues")
plt.show()

# 수치 입력
sns.heatmap(pivot_data, cmap="Blues", annot = True)
plt.show()


# 정수 형태로 출력
sns.heatmap(pivot_data, cmap="Blues", annot = True, fmt = 'd')
plt.show()


# -------------------------------------------------------------------------










# colorbar 가로로 놓기 --------------------------------------------------
# 비교해서 볼 것

'''
----------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('flights')
sns.set(rc={'figure.figsize':(10, 5)})

print(df ,'\n')
print(df.head(10) ,'\n')

# heatmap 에 사용할 수 있도록 데이터 형태 변경
pivot_data = df.pivot("month", "year", "passengers")

#sns.heatmap(pivot_data)
sns.heatmap(pivot_data, linewidths=.5)  # 구분선 추가
plt.show()
----------------------------------------------------
'''




import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('flights')
sns.set(rc={'figure.figsize':(10, 5)})

print(df ,'\n')
print(df.head(10) ,'\n')

pivot_data = df.pivot("month", "year", "passengers")

# fig 만들고 세부설정을 하고 subplots(2) 두 개 만든다. 
fig, (ax, cbar_ax) = plt.subplots(2)

ax = sns.heatmap(pivot_data, ax=ax,
                  cbar_ax=cbar_ax,
                  cbar_kws={"orientation": "horizontal"})

plt.show()

# -------------------------------------------------------------------------







# orientation : vertical -------------------------------------------------


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('flights')
sns.set(rc={'figure.figsize':(10, 5)})

print(df ,'\n')
print(df.head(10) ,'\n')

pivot_data = df.pivot("month", "year", "passengers")
fig, (ax, cbar_ax) = plt.subplots(2)
ax = sns.heatmap(pivot_data, ax=ax,
                  cbar_ax=cbar_ax,
                  cbar_kws={"orientation": "vertical"})
plt.show()


# --------------------------------------------------------------------



# 최종 ------------------------------------------------------------


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('flights')
sns.set(rc={'figure.figsize':(10, 5)})

print(df ,'\n')
print(df.head(10) ,'\n')

pivot_data = df.pivot("month", "year", "passengers")

grid_kws = {"height_ratios": (.85, .1), "hspace": 0.4}

f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)
ax = sns.heatmap(pivot_data, ax=ax,
                 cbar_ax=cbar_ax,
                 cbar_kws={"orientation": "horizontal"},
                 cmap="Blues", 
                 annot = True, fmt = 'd')
plt.show()



# -------------------------------------------------------------------------



