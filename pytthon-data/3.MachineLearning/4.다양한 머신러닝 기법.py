import seaborn as sns
import pandas as pd

df = sns.load_dataset('titanic')

train_df = df[:800]
test_df = df[800:]

names = train_df.columns
train_df = train_df.drop(names[4:], axis = 1)
test_df = test_df.drop(names[4:], axis = 1)

train_df.fillna(train_df.mean()[['age']], inplace = True)
test_df.fillna(test_df.mean()[['age']], inplace = True)

map_dict = {'female' : 0, 'male' : 1}

train_df['sex'] = train_df['sex'].map(map_dict).astype(int)
test_df['sex'] = test_df['sex'].map(map_dict).astype(int)

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

X_train = train_df.drop(["survived"], axis=1)
Y_train = train_df["survived"]
X_test  = test_df.drop("survived", axis=1)
Y_test = test_df["survived"]




# 결정나무
from sklearn.tree import DecisionTreeClassifier

decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, Y_train)

print(decision_tree.score(X_train, Y_train))
print(decision_tree.score(X_test, Y_test))

'''
학습하다가 오류가 나버리면 결과를 신뢰할 수 없게 된다.
'''




# 배깅(랜덤 포레스트)
# 하나의 데이터에서 랜덤으로 몇개의 샘플링을 여러개 만들어서 모델을 만들어서 가공후에 최종 모델을 만들어 사용하는 방식
# 훨씬 더 정확하다

from sklearn.ensemble import RandomForestClassifier
random_forest = RandomForestClassifier(n_estimators=100)  # 랜덤 모델을 100개 만든다
random_forest.fit(X_train, Y_train)                       # 학습
print(random_forest.score(X_train, Y_train))
print(random_forest.score(X_test, Y_test))




# 부스팅(xgboost)
# 특정 데이터의 결점이 있을 시 결점을 보완해가면서 샘플 모델을 만들어서 최종 모델을 만들어 사용하는 방식

import xgboost as xgb
boosting_model = xgb.XGBClassifier(n_estimators = 100)
boosting_model.fit(X_train, Y_train)
print(boosting_model.score(X_train, Y_train))
print(boosting_model.score(X_test, Y_test))
















