# 결측값 :  알려지지 않고, 수집되지 않거나 잘못 입력된 데이터 세트의 값

# 여기서도 inplace=True 는 동일하게 작동한다. (판다스 내의 거의 모든 함수에 있는 보통 옵션) 


# 결측값의 표현과 유무-------------------------------------------------------------------------
# 결측값은 np.nan 으로 표현함 
# 판다스 변수명.isnull() 결측값을 참,거짓으로 보여줌
# sum 은 사용법 동일

import pandas as pd
import numpy as np

df = pd.DataFrame({'a' : [1, 1, 3, 4, 5], 'b' : [2, 3, np.nan, 3, 4], 'c' : [3, 4, 7, 6, 4]})

print(df,'\n')
print(df.isnull(),'\n')
print(df.isnull().sum(),'\n')



'''
   a    b  c
0  1  2.0  3
1  1  3.0  4
2  3  NaN  7
3  4  3.0  6
4  5  4.0  4 

       a      b      c
0  False  False  False
1  False  False  False
2  False   True  False
3  False  False  False
4  False  False  False 

a    0
b    1
c    0
dtype: int64 

'''

# --------------------------------------------------------------------------------




#  결측값이 포함된 행/열 지우기 ------------------------------------------------
# 판다스 변수명.dropna  	      >>	 결측값이 포함된 행을 지우기
# 판다스 변수명.dropna(axis=1)   >>	 결측값이 포함된 열을 지우기


import pandas as pd
import numpy as np

df = pd.DataFrame({'a' : [1, 1, 3, 4, 5], 'b' : [2, 3, np.nan, 3, 4], 'c' : [3, 4, 7, 6, 4]})
print(df,'\n')
df.dropna(inplace=True)
print(df,'\n')


df = pd.DataFrame({'a' : [1, 1, 3, 4, 5], 'b' : [2, 3, np.nan, 3, 4], 'c' : [3, 4, 7, 6, 4]})
df.dropna(axis=1 ,inplace=True)
print(df,'\n')


'''
   a    b  c
0  1  2.0  3
1  1  3.0  4
2  3  NaN  7
3  4  3.0  6
4  5  4.0  4 

결측값 2번 행 지움
   a    b  c
0  1  2.0  3
1  1  3.0  4
3  4  3.0  6
4  5  4.0  4 

결측값 b 열 지움
   a  c
0  1  3
1  1  4
2  3  7
3  4  6
4  5  4 

'''

# --------------------------------------------------------------------------------









# 특정값으로 대체하기----------------------------------------------------------
# 판다스 변수명.fillna(바꿀 값)  >>  결측값을 바꿀 값으로 바꾼다.
'''
각종 method
method='bfill'   >>   뒤의 값으로 채우기
method='ffill'    >>   앞의 값으로 채우기

'''


import pandas as pd
import numpy as np

df = pd.DataFrame({'a' : [1, 1, 3, 4, 5], 'b' : [2, 3, np.nan, 3, 4], 'c' : [3, 4, 7, 6, 4]})
print(df,'\n')
df.fillna(3333, inplace=True)
print(df,'\n')



df = pd.DataFrame({'a' : [1, 1, 3, 4, np.nan], 'b' : [2, 3, np.nan, np.nan, 4], 'c' : [np.nan, 4, 1, 1, 4]})
print(df,'\n')
df.fillna(method='bfill' , inplace=True)
print(df,'\n')



df = pd.DataFrame({'a' : [1, 1, 3, 4, np.nan], 'b' : [2, 3, np.nan, np.nan, 4], 'c' : [np.nan, 4, 1, 1, 4]})
print(df,'\n')
df.fillna(method='ffill' , inplace=True)
print(df,'\n')




'''
원본
     a    b    c
0  1.0  2.0  NaN
1  1.0  3.0  4.0
2  3.0  NaN  1.0
3  4.0  NaN  1.0
4  NaN  4.0  4.0 


특정값으로 바꾸기
   a       b  c
0  1     2.0  3
1  1     3.0  4
2  3  3333.0  7
3  4     3.0  6
4  5     4.0  4 

원본
     a    b    c
0  1.0  2.0  NaN
1  1.0  3.0  4.0
2  3.0  NaN  1.0
3  4.0  NaN  1.0
4  NaN  4.0  4.0 

뒤에거로 바꾸기
     a    b    c
0  1.0  2.0  4.0
1  1.0  3.0  4.0
2  3.0  4.0  1.0
3  4.0  4.0  1.0
4  NaN  4.0  4.0 

원본
     a    b    c
0  1.0  2.0  NaN
1  1.0  3.0  4.0
2  3.0  NaN  1.0
3  4.0  NaN  1.0
4  NaN  4.0  4.0 

앞에거로 바꾸기
     a    b    c
0  1.0  2.0  NaN
1  1.0  3.0  4.0
2  3.0  3.0  1.0
3  4.0  3.0  1.0
4  4.0  4.0  4.0 


'''


# --------------------------------------------------------------------------------











# 제한 --------------------------------------------------------------------
# 각 열마다 바꿀 결측값 갯수를 제한할 수 있다.
# 먼저 나온 순으로 변경

import pandas as pd
import numpy as np

df = pd.DataFrame({'a' : [1, 1, 3, 4, np.nan], 'b' : [2, 3, np.nan, np.nan, 4], 'c' : [np.nan, 4, 1, 1, 4]})
print(df,'\n')
df.fillna(method='ffill' , inplace=True , limit =1)
print(df,'\n')


'''
     a    b    c
0  1.0  2.0  NaN
1  1.0  3.0  4.0
2  3.0  NaN  1.0
3  4.0  NaN  1.0
4  NaN  4.0  4.0 

     a    b    c
0  1.0  2.0  NaN
1  1.0  3.0  4.0
2  3.0  3.0  1.0
3  4.0  NaN  1.0
4  4.0  4.0  4.0 


'''

# --------------------------------------------------------------------------------




# 평균 ----------------------------------------------------------------------



import pandas as pd
import numpy as np


df = pd.DataFrame({'a' : [1, 1, 3, 4, np.nan], 'b' : [2, 3, np.nan, np.nan, 4], 'c' : [np.nan, 4, 1, 1, 4]})
df.mean()['a']
print(df,'\n')
df.fillna(df.mean()['a'] , inplace=True)
print(df,'\n')
print(df.mean(),'\n')




df = pd.DataFrame({'a' : [1, 1, 3, 4, np.nan], 'b' : [2, 3, np.nan, np.nan, 4], 'c' : [np.nan, 4, 1, 1, 4]})
print(df,'\n')
df.fillna(df.mean()[['b','c']] , inplace=True)
print(df,'\n')
df.fillna(df.mean()[['a','b','c']] , inplace=True)
print(df,'\n')


'''
원본
     a    b    c
0  1.0  2.0  NaN
1  1.0  3.0  4.0
2  3.0  NaN  1.0
3  4.0  NaN  1.0
4  NaN  4.0  4.0 

a의 평균값으로 결측값을 바꿈
      a     b     c
0  1.00  2.00  2.25
1  1.00  3.00  4.00
2  3.00  2.25  1.00
3  4.00  2.25  1.00
4  2.25  4.00  4.00 

각 열마다 평균 출력
a    2.25
b    2.70
c    2.45
dtype: float64 

원본
     a    b    c
0  1.0  2.0  NaN
1  1.0  3.0  4.0
2  3.0  NaN  1.0
3  4.0  NaN  1.0
4  NaN  4.0  4.0 

b와 c의 평균대입
     a    b    c
0  1.0  2.0  2.5
1  1.0  3.0  4.0
2  3.0  3.0  1.0
3  4.0  3.0  1.0
4  NaN  4.0  4.0 

a와 b와 c의 평균대입
    a    b    c
0  1.00  2.0  2.5
1  1.00  3.0  4.0
2  3.00  3.0  1.0
3  4.00  3.0  1.0
4  2.25  4.0  4.0 

'''
# --------------------------------------------------------------------------------
















