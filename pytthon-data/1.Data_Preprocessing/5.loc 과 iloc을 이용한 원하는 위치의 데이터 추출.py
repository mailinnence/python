
# 반복문을 이용한 데이터 생성---------------------------------------------

import pandas as pd
df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]})
print(df)



'''
    a   b   c
0   1  11  21
1   2  12  22
2   3  13  23
3   4  14  24
4   5  15  25
5   6  16  26
6   7  17  27
7   8  18  28
8   9  19  29
9  10  20  30
'''


# --------------------------------------------------------------------------------






# 두 개 이상의 칼럼의 데이터를 출력----------------------------------------

import pandas as pd
df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]})

try:
    print(df['a', 'b'])
except:
    print('error')


'''
error
이렇게 데이터를 출력하는 걸로 실수를 많이 하는데 
이렇게 출력하는 하는 것이 아니다.
'''




-------------------------
import pandas as pd
df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]})

print(df[['a', 'b']],"\n")
print(type(df[['a', 'b']]))



'''
    a   b
0   1  11
1   2  12
2   3  13
3   4  14
4   5  15
5   6  16
6   7  17
7   8  18
8   9  19
9  10  20

<class 'pandas.core.frame.DataFrame'>
시리즈가 아니다.
'''
# --------------------------------------------------------------------------------





# 출력--------------------------------------------------------------------------

# 전체 출력
import pandas as pd
df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]})
print(df)



'''    
     a   b   c
0   1  11  21
1   2  12  22
2   3  13  23
3   4  14  24
4   5  15  25
5   6  16  26
6   7  17  27
7   8  18  28
8   9  19  29
9  10  20  30

'''




# 칼럼에 해당하는 데이터 출력 >> 시리즈로 나옴

import pandas as pd
df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]})
print(df['a'])

'''
0     1
1     2
2     3
3     4
4     5
5     6
6     7
7     8
8     9
9    10
Name: a, dtype: int64


'''


# 인데스에 해당하는 데이터 출력 
# --틀린 예시--
import pandas as pd
df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]})
print(df[0])

'''
error
이렇게 출력하는 것이 아니다.
'''


# --옳바른 예시--
import pandas as pd
df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]})
print(df,'\n')
print(df.loc[0])

'''
     a   b   c
0   1  11  21
1   2  12  22
2   3  13  23
3   4  14  24
4   5  15  25
5   6  16  26
6   7  17  27
7   8  18  28
8   9  19  29
9  10  20  30 

a     1
b    11
c    21
Name: 0, dtype: int64

'''






# --범위형--

import pandas as pd
df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]})
print(df,'\n')
print(df.loc[0:4])


'''
    a   b   c
0   1  11  21
1   2  12  22
2   3  13  23
3   4  14  24
4   5  15  25
5   6  16  26
6   7  17  27
7   8  18  28
8   9  19  29
9  10  20  30 

   a   b   c
0  1  11  21
1  2  12  22
2  3  13  23
3  4  14  24
4  5  15  25

'''





# --세밀한 범위형--

import pandas as pd
index = ['A', 'B', 'D', 'C', 'E', 'F', 'G', 'G', 'H', 'I']
df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]} ,index=index )
print(df,'\n')
print(df.loc[['G', 'I'], ['a', 'c']])           # df.loc[[열], [행]]  

'''
     a   b   c
A   1  11  21
B   2  12  22
D   3  13  23
C   4  14  24
E   5  15  25
F   6  16  26
G   7  17  27
G   8  18  28
H   9  19  29
I  10  20  30 

    a   c
G   7  27
G   8  28
I  10  30

'''
# --------------------------------------------------------------------------------










# 처음부터 5번째 까지의 데이터와 첫 번째 열과 세 번째 열의 데이터를 추출하시오.

import pandas as pd
df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]})
print(df,"\n")
print(df.iloc[:5, [0, 2]])         # df.iloc[:n, [0, n]]  >> n-1 까지만 출력

'''
     a   b   c
0   1  11  21
1   2  12  22
2   3  13  23
3   4  14  24
4   5  15  25
5   6  16  26
6   7  17  27
7   8  18  28
8   9  19  29
9  10  20  30 

    a   c
0  1  21
1  2  22
2  3  23
3  4  24
4  5  25

'''

# --------------------------------------------------------------------------------




