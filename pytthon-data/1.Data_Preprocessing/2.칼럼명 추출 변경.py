# 칼럼명 추출 / 변경 --------------------------------------------------------------
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})
print(df,"\n")
print(df.columns,"\n")     # 전체 칼럼 부르기 (가로)
print(df.columns[1],"\n")  # 특정 칼럼 부르기 (가로)


'''
   a  b  c
0  1  4  7
1  2  5  8
2  3  6  9 

Index(['a', 'b', 'c'], dtype='object') 

b 
'''


import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})
print(df,"\n")
print(df.columns,"\n")     # 전체 칼럼 부르기 (가로)
print(df.columns[1],"\n")  # 특정 칼럼 부르기 (가로)

df.columns = ['d', 'e', 'f'] # 칼럼 바꾸기 (가로)

print(df)




'''
   a  b  c
0  1  4  7
1  2  5  8
2  3  6  9 

Index(['a', 'b', 'c'], dtype='object') 

b 

   d  e  f
0  1  4  7
1  2  5  8
2  3  6  9

'''
# --------------------------------------------------------------------------------








# rename 을 통한 칼럼명 변경 ------------------------------------------------------
import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})
df.columns = ['d', 'e', 'f']

df1=df.rename(columns = {'d' : '디', 'f' : '에프'})     # 바로 저장이 되지 않아 변수에 저장함
print(df,"\n")
print(df1)


'''
   d  e  f
0  1  4  7
1  2  5  8
2  3  6  9

   디  e   에프
0  1   4   7
1  2   5   8
2  3   6   9

'''




import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})
df.columns = ['d', 'e', 'f']

print(df,"\n")

df.rename(columns = {'d' : '디', 'f' : '에프'}, inplace = True)
print(df)


'''
   d  e  f
0  1  4  7
1  2  5  8
2  3  6  9 

   디  e   에프
0  1   4   7
1  2   5   8
2  3   6   9
'''



# ex)

import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})
df.rename(columns = {'a' : '에이'}, inplace = True)
print(df)

'''
      에이  b  c
0     1     4  7
1     2     5  8
2     3     6  9

'''

# --------------------------------------------------------------------------------
