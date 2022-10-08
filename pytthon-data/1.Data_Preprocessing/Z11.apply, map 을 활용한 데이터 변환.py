#  a 가 2 보다 작으면 '2 미만', 4 보다 작으면 '4 미만', 4 보다 --------------
#  크면 '4 이상' 이 저장된 b 칼럼을 추가하시오. -----------------------------



import pandas as pd

df = pd.DataFrame({'a' : [1, 2, 3, 4, 5]})

df['b'] = 0
a = df[df['a'] < 2]
print(a,'\n')
df['b'][a.index] = '2 미만'
'''
현재 a는  
  ab
0 10  이 상태이다.
때문에 b[0]과 동일하다.
'''
print(df,'\n')


a = df[(df['a'] >= 2) & (df['a'] < 4)]
print(a,'\n')



'''
   a  b
0  1  0 

   a     b
0  1  2 미만
1  2     0
2  3     0
3  4     0
4  5     0 

   a  b
1  2  0
2  3  0 

'''


# ---------------------------------------------------------------------------






# 유용한 기능-------------------------------------------------------------
'''
여기서 
df=df['b'][a.index] = '4 미만'
을 하면 오류가 뜬다. 한번에 두개 이상씩 바꿀때는
pd.set_option('mode.chained_assignment',  None)
해주면 해당 내용만 
'''





import pandas as pd

df = pd.DataFrame({'a' : [1, 2, 3, 4, 5]})

df['b'] = 0
a = df[df['a'] < 2]
print(a,'\n')
df['b'][a.index] = '2 미만'
'''
현재 a는  
  ab
0 10  이 상태이다.
때문에 b[0]과 동일하다.
'''
print(df,'\n')


a = df[(df['a'] >= 2) & (df['a'] < 4)]
print(a,'\n')


pd=pd.set_option('mode.chained_assignment',  None)
df['b'][a.index] = '4 미만'
print(df)



'''
    a  b
0  1  0 

   a     b
0  1  2 미만
1  2     0
2  3     0
3  4     0
4  5     0 

   a  b
1  2  0
2  3  0 

   a     b
0  1  2 미만
1  2  4 미만
2  3  4 미만
3  4     0
4  5     0


'''



# ex) 다른방법



import pandas as pd

df = pd.DataFrame({'a' : [1, 2, 3, 4, 5]})
df['b'] = 0
a = df[df['a'] >= 4]
df['b'][a.index] = '4 이상'
print(df)


'''
   a     b
0  1     0
1  2     0
2  3     0
3  4  4 이상
4  5  4 이상

'''


# ---------------------------------------------------------------------------






# 함수 + apply 를 이용한 해결------------------------------------------
# 한번의 여러값을 넣는 것을 apply를 이용할 수도 있다
# apply   >>   함수에 넣을 값.apply(함수)



import pandas as pd

df = pd.DataFrame({'a' : [1, 2, 3, 4, 5]})

def case_function(x):
    if x < 2:
        return '2 미만'
    elif x < 4:
        return '4 미만'
    else:
        return '4 이상


def function(x):
    if x == 1:
        return 'one'
    elif x == 2:
        return 'two'
    elif x == 3:
        return 'three'
    elif x == 4:
        return 'four'
    elif x == 5:
        return 'five'



df['c'] = df['a'].apply(case_function)
df['d'] = df['a'].apply(function)
print(df,'\n')


'''
    a      c          d
0   1   2 미만     one
1   2   4 미만     two
2   3   4 미만    three
3   4   4 이상     four
4   5   4 이상     five 


'''



# ---------------------------------------------------------------------------







# map 을 이용한 해결 방법----------------------------------------------
# map 을 이용하여 딕션너리를 value 값을 대입시킬 수 있다.

import pandas as pd

df = pd.DataFrame({'a' : [1, 2, 3, 4, 5]})
a = { 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five'}
df['e'] = df['a'].map(a)
print(df,'\n')


'''
   a      e
0  1    one
1  2    two
2  3   three
3  4    four
4  5    five 


'''


# ---------------------------------------------------------------------------
