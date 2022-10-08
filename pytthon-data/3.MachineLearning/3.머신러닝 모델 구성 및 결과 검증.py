
'''
주어진 데이터에서 생존자의 여부를 파악하는 AI 를 만드는 것
'''


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

train_df = df[:800]
test_df = df[800:]


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

'''
 survived  pclass  sex  age
0         0       3    1    2
1         1       1    0    2
2         1       3    0    2
3         1       1    0    2
4         0       3    1    2
5         0       3    1    2
6         0       1    1    3
7         0       3    1    1
8         1       3    0    2
9         1       2    0    1

     survived  pclass  sex  age
800         0       2    1    2
801         1       2    0    2
802         1       1    1    1
803         1       3    1    1
804         1       3    1    2
805         0       3    1    2
806         0       1    1    2
807         0       3    0    1
808         0       2    1    2
809         1       1    0    2

'''




# 결론 상관관계가 있는 애들만 남기고 데이터를 가공하기 쉽게
#   결측값은 없애고 문자열은 숫자형으로 바꾸고 범위화 하였다.










# 라이브러러를 이용해서 분류를 할 예정
from sklearn.tree import DecisionTreeClassifier
import pandas as pd


#  데이터 분류
# X변수에는 survived 제거 Y변수는 그대로
# 훈련시킨것과 물리적으로 그대로 가공된 것을 비교해서 loss 값이 낮아야 정확도가 높을테고 
# 그래야 새로운데이터도 판단할 수 있기 때문
X_train = train_df.drop(["survived"], axis=1)
Y_train = train_df["survived"]
X_test  = test_df.drop("survived", axis=1)
Y_test = test_df["survived"]


print(X_train.head(),'\n')
print(Y_train.head(),'\n')




# 모델 생성 및 학습(decision tree 사용)
# 변수에 해당 라이브러리 함수를 가져오고
decision_tree = DecisionTreeClassifier()
# 훈련변수를 트레이닝 decision_tree.fit(예상 , 정답)
decision_tree.fit(X_train, Y_train)


# 모델 정확도 검증	 >>  거의 비슷하게 나옴
print(decision_tree.score(X_train, Y_train))
print(decision_tree.score(X_test, Y_test))

'''
0.8
0.7692307692307693

'''




#실제값 예측값 비교 구현 >> 위 방식은 decision_tree.score() 함수를 쓰지 않고 예측값을 비교하는 과정
Y_pred = decision_tree.predict(X_test)
print(Y_pred)

print(Y_test)


'''
예측값
0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 1 0 0 0 0 0 1 1 0 0 0 0 1 0
 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 1 1 1 1 1 0 1 0 0 0 1 1 0 1 1 0 0 0 0 1 0 0
 1 1 0 0 0 1 1 0 1 0 0 1 0 1 1 0 0]

실제값
800    0
801    1
802    1
803    1
804    1
      ..
886    0
887    1
888    0
889    1
890    0
'''

len(Y_pred)	#예측값
len(Y_test)	#실제값

#비교하기 편하게 실제값을 리스트로 만들어놓으라
Y_test_list = list(Y_test)


total = 0
for i in range(len(Y_pred)):
    if Y_pred[i] == Y_test_list[i]:
        total += 1
    else:
        pass

print(total)		# 실제값 == 예측값 동일 한 갯수
print(total / len(Y_pred))	# (실제값 == 예측값 동일 한 갯수) 의 평균


#  graphviz 를 이용한 tree 구조 시각화



from sklearn.tree import export_graphviz

export_graphviz(
        decision_tree,			# 사용한 학습 방법
        out_file = "titanic.dot",			# 출력파일
        feature_names = ['pclass', 'sex', 'age'],	# 특징 분류
        class_names = ['Unsurvived','Survived'],	# 클래스
        filled=True				# 그림 색깔 유무 (유 = True) 
    )

import graphviz
f = open('titanic.dot')
dot_graph = f.read()
# 자원을 효율적으로 쓰기 위해서는 아래 주석 처리 된 코드 사용
#with open("titanic.dot") as f:
#   dot_graph = f.read()
dot = graphviz.Source(dot_graph)
dot.format = 'png'
dot.render(filename = 'titanic_tree')
dot





