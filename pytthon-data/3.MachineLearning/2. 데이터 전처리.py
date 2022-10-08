import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

train_df = df[:800]
test_df = df[800:]


print(len(train_df))
print(len(test_df))



print(df.head(20))



'''
    survived  pclass     sex   age  sibsp  parch     fare embarked   class    who  adult_male deck  embark_town alive  alone
0          0       3    male  22.0      1      0   7.2500        S   Third    man        True  NaN  Southampton    no  False
1          1       1  female  38.0      1      0  71.2833        C   First  woman       False    C    Cherbourg   yes  False
2          1       3  female  26.0      0      0   7.9250        S   Third  woman       False  NaN  Southampton   yes   True
3          1       1  female  35.0      1      0  53.1000        S   First  woman       False    C  Southampton   yes  False
4          0       3    male  35.0      0      0   8.0500        S   Third    man        True  NaN  Southampton    no   True
5          0       3    male   NaN      0      0   8.4583        Q   Third    man        True  NaN   Queenstown    no   True
6          0       1    male  54.0      0      0  51.8625        S   First    man        True    E  Southampton    no   True
7          0       3    male   2.0      3      1  21.0750        S   Third  child       False  NaN  Southampton    no  False
8          1       3  female  27.0      0      2  11.1333        S   Third  woman       False  NaN  Southampton   yes  False
9          1       2  female  14.0      1      0  30.0708        C  Second  child       False  NaN    Cherbourg   yes  False
10         1       3  female   4.0      1      1  16.7000        S   Third  child       False    G  Southampton   yes  False
11         1       1  female  58.0      0      0  26.5500        S   First  woman       False    C  Southampton   yes   True
12         0       3    male  20.0      0      0   8.0500        S   Third    man        True  NaN  Southampton    no   True
13         0       3    male  39.0      1      5  31.2750        S   Third    man        True  NaN  Southampton    no  False
14         0       3  female  14.0      0      0   7.8542        S   Third  child       False  NaN  Southampton    no   True
15         1       2  female  55.0      0      0  16.0000        S  Second  woman       False  NaN  Southampton   yes   True
16         0       3    male   2.0      4      1  29.1250        Q   Third  child       False  NaN   Queenstown    no  False
17         1       2    male   NaN      0      0  13.0000        S  Second    man        True  NaN  Southampton   yes   True
18         0       3  female  31.0      1      0  18.0000        S   Third  woman       False  NaN  Southampton    no  False
19         1       3  female   NaN      0      0   7.2250        C   Third  woman       False  NaN    Cherbourg   yes   True
'''



train_df = df[:800]
test_df = df[800:]

print(len(train_df))
print(len(test_df))

a=train_df[['pclass', 'survived']].groupby(['pclass'], as_index=False).mean().sort_values(by='survived', ascending=False)
print(a)



'''
1.'pclass', 'survived' 를  pclass 로 그룹화를 시킨다 
2.해당 survived  평균값을 넣는다
3.survived 를 기준으로 오름차순으로 정렬한다.
'''

# 그룹을 index 로 사용하고 싶지 않은 경우에는 as_index = False 로 설정


'''
   pclass  survived
0       1  0.615385
1       2  0.481928
2       3  0.246014

깔끔하다.
즉 관계가 있을 것이다.
'''




# sibsp 와 survived 의 관계(관계가 적음)

a=train_df[["sibsp", "survived"]].groupby(['sibsp'], as_index=False).mean().sort_values(by='survived', ascending=False)
print(a)


'''
  sibsp  survived
1      1  0.518325
2      2  0.481481
0      0  0.348708
3      3  0.266667
4      4  0.200000
5      5  0.000000
6      8  0.000000

세 그룹이 0이다.
sibsp 와 비례 또는 반비례 관계도 찾기 힘들다
맞아떨어지는 감이 없다. 
관계가 적다.
'''





# age 와 survived 의 관계

a=train_df[["age", "survived"]].groupby(['age'], as_index=False).mean().sort_values(by='survived', ascending=False)
print(a)


'''

세 그룹이 0이다.
sibsp 와 비례 또는 반비례 관계도 찾기 힘들다

   sibsp  survived
      age  survived
0    0.67       1.0
8    5.00       1.0
77  63.00       1.0
66  53.00       1.0
1    0.75       1.0
..    ...       ...
25  20.50       0.0
39  30.50       0.0
36  28.50       0.0
31  24.50       0.0
47  36.50       0.0

..... 양이 많아 모르겠다...
이럴때는 그래프를 이용한다!
'''


sns.histplot(data = train_df, x = 'age', bins = 20, hue = 'survived')
plt.show()


a = sns.FacetGrid(train_df, col='survived')
a.map(plt.hist, 'age', bins=20)
plt.show()

'''
관계가 있어 보인다.
'''



# pclass 에 따른 age 별 survived 유무

a = sns.FacetGrid(train_df, col='survived', row='pclass')
a.map(plt.hist, 'age', bins=20)
plt.show()

'''
survived' 와 'pclass'
의 모든 경우에 해당하는 age 분포 파악
'''






# 필요없는 필드 삭제
names = train_df.columns
print(names,'\n')

train_df = train_df.drop(names[4:], axis = 1)
print(train_df.head(),'\n')

test_df = test_df.drop(names[4:], axis = 1)
print(test_df.head() ,'\n')


# 결측값 확인
print(train_df.isnull().sum())
print(test_df.isnull().sum() ,'\n')





#age 평균으로 age 결측값 채우기
train_df.fillna(train_df.mean()[['age']], inplace = True)
test_df.fillna(test_df.mean()[['age']], inplace = True)

print(train_df.isnull().sum())
print(test_df.isnull().sum())




# 성별 인코딩 >> 데이터 가공은 문자열 보다 숫자형이 좋다
map_dict = {'female' : 0, 'male' : 1}

# 해당 변수에 딕션너리를 map으로 넣었음 values 값들이 들어감
train_df['sex'] = train_df['sex'].map(map_dict).astype(int)
test_df['sex'] = test_df['sex'].map(map_dict).astype(int)


print(train_df.head(),'\n')




# 나이 분류
def function1(x):
    if x < 20:
        return 1
    elif x < 40:
        return 2
    elif x < 60:
        return 3
    else:
        return 4

train_df['age'] = train_df['age'].apply(function1)
test_df['age'] = test_df['age'].apply(function1)








print(train_df.head(10),'\n')
print(test_df.head(10) ,'\n')


# 결론 상관관계가 있는 애들만 남기고 데이터를 가공하기 쉽게
   결측값은 없애고 문자열은 숫자형으로 바꾸고 범위화 하였다.



