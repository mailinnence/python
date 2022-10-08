


# 상하 결합--------------------------------------------------------------------
# 옵션에  ignore_index = True 을 추가하면 인덱스가 초기화 된다



import pandas as pd

df1 = pd.DataFrame({'A' : [1, 2, 3], 'B' : [11, 12, 13], 'C' : [21, 22, 23]})
print(df1,'\n')
df2 = pd.DataFrame({'A' : [4, 5, 6], 'B' : [14, 15, 16], 'C' : [24, 25, 26]})
print(df2,'\n')

print(pd.concat([df1, df2]))
print(pd.concat([df2, df1]))
print(pd.concat([df1, df2], ignore_index = True))

'''
   A   B   C
0  1  11  21
1  2  12  22
2  3  13  23

   A   B   C
0  4  14  24
1  5  15  25
2  6  16  26

   A   B   C
0  1  11  21
1  2  12  22
2  3  13  23
0  4  14  24
1  5  15  25
2  6  16  26

   A   B   C
0  4  14  24
1  5  15  25
2  6  16  26
0  1  11  21
1  2  12  22
2  3  13  23

   A   B   C
0  1  11  21
1  2  12  22
2  3  13  23
3  4  14  24
4  5  15  25
5  6  16  26
'''




# --------------------------------------------------------------------------------





# 필드의 순서가 섞였을 때 결합 결과 확인----------------------------------


import pandas as pd
df1 = pd.DataFrame({'A' : [1, 2, 3], 'B' : [11, 12, 13], 'C' : [21, 22, 23]})
df2 = pd.DataFrame({'B' : [14, 15, 16], 'A' : [4, 5, 6], 'C' : [24, 25, 26]})

print(pd.concat([df1, df2]))



'''
  A   B   C
0  1  11  21
1  2  12  22
2  3  13  23
0  4  14  24
1  5  15  25
2  6  16  26

섞여있어도 알아서 들어감
'''
# --------------------------------------------------------------------------------




# 서로 다른 필드로 구성되어 있는 데이터 프레임의 결합------------------

import pandas as pd
df1 = pd.DataFrame({'A' : [1, 2, 3], 'B' : [11, 12, 13], 'C' : [21, 22, 23], 'D' : [31, 32, 33]})
df2 = pd.DataFrame({'A' : [3, 4, 5], 'B' : [13, 14, 15], 'C' : [23, 24, 25], 'E' : [41, 42, 43]})

print(pd.concat([df1, df2]) , '\n')
print(pd.concat([df1, df2], join = 'outer'), '\n')
print(pd.concat([df1, df2], join = 'inner') , '\n')

'''
더해짐
   A   B   C     D     E
0  1  11  21  31.0   NaN       없는 값은 결측값 처리됨
1  2  12  22  32.0   NaN
2  3  13  23  33.0   NaN
0  3  13  23   NaN  41.0
1  4  14  24   NaN  42.0
2  5  15  25   NaN  43.0

outer 
   A   B   C     D     E
0  1  11  21  31.0   NaN
1  2  12  22  32.0   NaN
2  3  13  23  33.0   NaN
0  3  13  23   NaN  41.0
1  4  14  24   NaN  42.0
2  5  15  25   NaN  43.0

inner 결측값이 있는 칼럼 제외하고 보여줌
   A   B   C
0  1  11  21
1  2  12  22
2  3  13  23
0  3  13  23
1  4  14  24
2  5  15  25


'''


# --------------------------------------------------------------------------------














# 좌우 결합--------------------------------------------------------------------

import pandas as pd

df1 = pd.DataFrame({'A' : [1, 2, 3], 'B' : [11, 12, 13], 'C' : [21, 22, 23], 'D' : [31, 32, 33]})
df2 = pd.DataFrame({'E' : [3, 4, 5], 'F' : [13, 14, 15], 'G' : [23, 24, 25], 'H' : [41, 42, 43]})

print(df1, '\n')

print(df2, '\n')


'''
aixs=0(index)     행
aixs=1(columns) 열
'''
print(pd.concat([df1, df2], axis = 1), '\n')
print(pd.concat([df1, df2], axis = 0))



'''
   A   B   C   D
0  1  11  21  31
1  2  12  22  32
2  3  13  23  33 

   E   F   G   H
0  3  13  23  41
1  4  14  24  42
2  5  15  25  43 

   A   B   C   D  E   F   G   H
0  1  11  21  31  3  13  23  41
1  2  12  22  32  4  14  24  42
2  3  13  23  33  5  15  25  43 

     A      B      C         D     E         F       G       H
0  1.0     11.0   21.0    31.0   NaN   NaN   NaN   NaN
1  2.0     12.0   22.0    32.0   NaN   NaN   NaN   NaN
2  3.0     13.0   23.0    33.0   NaN   NaN   NaN   NaN
0  NaN   NaN   NaN    NaN   3.0    13.0   23.0   41.0
1  NaN   NaN   NaN    NaN   4.0    14.0   24.0   42.0
2  NaN   NaN   NaN    NaN   5.0    15.0   25.0   43.0

'''

# --------------------------------------------------------------------------------




# 겹칠때------------------------------------------------------------------------


import pandas as pd


df1 = pd.DataFrame({'ID' : [1, 2, 3, 4, 5], '성별' : ['F', 'M', 'F', 'M', 'F'], '나이' : [20, 30, 40, 25, 42]})
df2 = pd.DataFrame({'ID' : [3, 4, 5, 6, 7], '키' : [160.5, 170.3, 180.1, 142.3, 153.7], '몸무게' : [45.1, 50.3, 72.1, 38,  42]})


print(pd.concat([df1, df2], axis = 1), '\n')


'''
   ID 성별  나이  ID      키   몸무게
0   1  F  20   3  160.5  45.1
1   2  M  30   4  170.3  50.3
2   3  F  40   5  180.1  72.1
3   4  M  25   6  142.3  38.0
4   5  F  42   7  153.7  42.0 

알아서 정리해줘용...

'''

# --------------------------------------------------------------------------------









# 성별과 나이가 확인 된 유저들을 대상으로 키와 몸무게의 정보를 결합하시오.

import pandas as pd

df1 = pd.DataFrame({'ID' : [1, 2, 3, 4, 5], '성별' : ['F', 'M', 'F', 'M', 'F'], '나이' : [20, 30, 40, 25, 42]})
df2 = pd.DataFrame({'ID' : [3, 4, 5, 6, 7], '키' : [160.5, 170.3, 180.1, 142.3, 153.7], '몸무게' : [45.1, 50.3, 72.1, 38,  42]})

print(df1, '\n')
print(df2, '\n')
print(pd.concat([df1, df2], axis = 1), '\n')
print(pd.merge(df1, df2, how = 'left', on = 'ID'))


'''
df1
   ID 성별  나이
0   1  F  20
1   2  M  30
2   3  F  40
3   4  M  25
4   5  F  42 

df2
   ID      키   몸무게
0   3  160.5  45.1
1   4  170.3  50.3
2   5  180.1  72.1
3   6  142.3  38.0
4   7  153.7  42.0 

df1,df2 의 결합
   ID 성별  나이  ID      키   몸무게
0   1  F  20   3  160.5  45.1
1   2  M  30   4  170.3  50.3
2   3  F  40   5  180.1  72.1
3   4  M  25   6  142.3  38.0
4   5  F  42   7  153.7  42.0 


성별과 나이가 확인 된 유저들을 대상으로 키와 몸무게의 정보를 결합
   ID 성별  나이      키   몸무게
0   1  F  20    NaN   NaN
1   2  M  30    NaN   NaN
2   3  F  40  160.5  45.1
3   4  M  25  170.3  50.3
4   5  F  42  180.1  72.1

'''





# --------------------------------------------------------------------------------




# 키와 몸무게가 확인 된 유저들을 대상으로 성별과 나이의 정보를 결합하시오.
'''
merge(a,b) 함수

a에다가 b를 추가 시키는 역할
'''




import pandas as pd


df1 = pd.DataFrame({'ID' : [1, 2, 3, 4, 5], '성별' : ['F', 'M', 'F', 'M', 'F'], '나이' : [20, 30, 40, 25, 42]})
df2 = pd.DataFrame({'ID' : [3, 4, 5, 6, 7], '키' : [160.5, 170.3, 180.1, 142.3, 153.7], '몸무게' : [45.1, 50.3, 72.1, 38,  42]})
print(pd.concat([df1, df2], axis = 1), '\n')

print(pd.merge(df2, df1, how = 'left', on = 'ID'), '\n')
print(pd.merge(df1, df2, how = 'right', on = 'ID'))

''' 
   ID 성별  나이  ID      키   몸무게
0   1  F  20   3  160.5  45.1
1   2  M  30   4  170.3  50.3
2   3  F  40   5  180.1  72.1
3   4  M  25   6  142.3  38.0
4   5  F  42   7  153.7  42.0 

   ID      키   몸무게   성별    나이
0   3  160.5  45.1    F  40.0
1   4  170.3  50.3    M  25.0
2   5  180.1  72.1    F  42.0
3   6  142.3  38.0  NaN   NaN
4   7  153.7  42.0  NaN   NaN 

   ID   성별    나이      키   몸무게
0   3    F  40.0  160.5  45.1
1   4    M  25.0  170.3  50.3
2   5    F  42.0  180.1  72.1
3   6  NaN   NaN  142.3  38.0
4   7  NaN   NaN  153.7  42.0
'''


# --------------------------------------------------------------------------------











# 모든 유저들의 정보를 출력하시오. --------------------------------------


import pandas as pd

df1 = pd.DataFrame({'USER_ID' : [1, 2, 3, 4, 5], '성별' : ['F', 'M', 'F', 'M', 'F'], '나이' : [20, 30, 40, 25, 42]})
df2 = pd.DataFrame({'ID' : [3, 4, 5, 6, 7], '키' : [160.5, 170.3, 180.1, 142.3, 153.7], '몸무게' : [45.1, 50.3, 72.1, 38,  42]})

print(pd.merge(df1, df2, how = 'outer', left_on = 'USER_ID', right_on = 'ID'))



'''
   USER_ID   성별    나이   ID      키   몸무게
0      1.0    F  20.0  NaN    NaN   NaN
1      2.0    M  30.0  NaN    NaN   NaN
2      3.0    F  40.0  3.0  160.5  45.1
3      4.0    M  25.0  4.0  170.3  50.3
4      5.0    F  42.0  5.0  180.1  72.1
5      NaN  NaN   NaN  6.0  142.3  38.0
6      NaN  NaN   NaN  7.0  153.7  42.0

'''

# --------------------------------------------------------------------------------



