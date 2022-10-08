
# 그룹화------------------------------------------------------------------------

# df2.groupby(by = ['칼럼명'])['칼럼의 대표 값']
# 그룹을 index 로 사용하고 싶지 않은 경우에는 as_index = False 로 설정



import pandas as pd
df1 = pd.DataFrame({'ID' : [1, 2, 3, 4, 5], '가입일' : ['2021-01-02', '2021-01-04', '2021-01-10', '2021-02-10', '2021-02-24'], '성별' : ['F', 'M', 'F', 'M', 'M']})
df2 = pd.DataFrame({'구매순서' : [1, 2, 3, 4, 5], 'ID' : [1, 1, 2, 4, 1], '구매월' : [1, 1, 2, 2, 3], '금액' : [1000, 1500, 2000, 3000, 4000]})


print(pd.merge(df1, df2, how = 'left', on = 'ID'),'\n')

print(df2.groupby(by = ['ID'])['금액'].sum(),'\n')
print(type(df2.groupby(by = ['ID'])['금액'].sum()) ,'\n')


print(df2.groupby(by = ['ID', '구매월'], as_index = False)['금액'].sum(),'\n')
print(type(df2.groupby(by = ['ID', '구매월'], as_index = False)['금액'].sum()),'\n')


'''
   ID         가입일 성별  구매순서  구매월      금액
0   1  2021-01-02  F   1.0  1.0  1000.0
1   1  2021-01-02  F   2.0  1.0  1500.0
2   1  2021-01-02  F   5.0  3.0  4000.0
3   2  2021-01-04  M   3.0  2.0  2000.0
4   3  2021-01-10  F   NaN  NaN     NaN
5   4  2021-02-10  M   4.0  2.0  3000.0
6   5  2021-02-24  M   NaN  NaN     NaN 

ID
1    6500
2    2000
4    3000
Name: 금액, dtype: int64 

<class 'pandas.core.series.Series'> 

   ID  구매월    금액
0   1    1  2500
1   1    3  4000
2   2    2  2000
3   4    2  3000 

<class 'pandas.core.frame.DataFrame'> 



'''

# --------------------------------------------------------------------------------














# df 는 각 회원의 구매 내역을 저장한 데이터 프레임이다. 각 회원의 누적 금액과 누적 구매 횟수를 회원 ID 별로 구하시오.

import pandas as pd
df = pd.DataFrame({'구매순서' : [1, 2, 3, 4, 5], 'ID' : [1, 1, 2, 4, 1], '구매월' : [1, 1, 2, 2, 3], '금액' : [1000, 1500, 2000, 3000, 4000], '수수료' : [100, 150, 200, 300, 400]})
df.groupby(by = ['ID'])['금액'].agg([sum, len])   # agg 을 이용하여 다수의 값 대입
print(df.groupby(by = ['ID'], as_index = False)['금액'].agg([sum, len]),'\n')
print(df.groupby(by = ['ID'])['금액'].agg([sum, len]),'\n')
df.reset_index(inplace = True)
df2 = df.groupby(by = ['ID'])['금액'].agg([sum, len])
df2.reset_index(inplace = True)
print(df2)

'''
     sum  len
ID           
1   6500    3
2   2000    1
4   3000    1 

     sum  len
ID           
1   6500    3
2   2000    1
4   3000    1 

   ID   sum  len
0   1  6500    3
1   2  2000    1
2   4  3000    1

'''





# --------------------------------------------------------------------------------



# df 는 각 회원의 구매 내역을 저장한 데이터 프레임이다. 각 회원의 최대 사용 금액 / 최소 사용 금액과 최저 수수료의 값을 구하시오.

import pandas as pd
df2 = pd.DataFrame({'구매순서' : [1, 2, 3, 4, 5], 'ID' : [1, 1, 2, 4, 1], '구매월' : [1, 1, 2, 2, 3], '금액' : [1000, 1500, 2000, 3000, 4000], '수수료' : [100, 150, 200, 300, 400]})

print(df2.groupby(by = ['ID']).agg({'금액' : [max, min], '수수료' : min}),'\n')

df2=df2.reset_index()
print(df2,'\n')

print(df2.columns,'\n')

print(df2.columns.values,'\n')
df2.columns = ['_'.join(col) for col in df2.columns.values]

print(df2.columns,'\n')
df2.reset_index()
print(df2,'\n')


'''
      금액        수수료
     max   min  min
ID                 
1   4000  1000  100
2   2000  2000  200
4   3000  3000  300 

   index  구매순서  ID  구매월    금액  수수료
0      0     1   1    1  1000  100
1      1     2   1    1  1500  150
2      2     3   2    2  2000  200
3      3     4   4    2  3000  300
4      4     5   1    3  4000  400 

Index(['index', '구매순서', 'ID', '구매월', '금액', '수수료'], dtype='object') 

['index' '구매순서' 'ID' '구매월' '금액' '수수료'] 

Index(['i_n_d_e_x', '구_매_순_서', 'I_D', '구_매_월', '금_액', '수_수_료'], dtype='object') 

   i_n_d_e_x  구_매_순_서  I_D  구_매_월   금_액  수_수_료
0          0        1    1      1  1000    100
1          1        2    1      1  1500    150
2          2        3    2      2  2000    200
3          3        4    4      2  3000    300
4          4        5    1      3  4000    400 


'''


# --------------------------------------------------------------------------------
























