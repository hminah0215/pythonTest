import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm, model_selection, neighbors
import random

df = pd.read_csv("day0424/iris.csv")

# 데이터를 섞어서 분리해주는 여러 라이브러리 중 sklearn , model_selection.train_test_split(문제, 답) 사용
# data = model_selection.train_test_split( df.iloc[:,0:4] ,  df.iloc[:,4] )
# print(type(data)) # <class 'list'>
# print(data[0])       #112 훈련시킬문제
# print(len(data[1])) # 38 테스트할문제
# print(data[2])      # 112 훈련에 대한 답
# print(len(data[3])) # 38 테스트의 답 

train_data, test_data, train_label, test_label = tuple(model_selection.train_test_split( df.iloc[:,0:4] ,  df.iloc[:,4] ))
print(len(train_data))  #112 훈련시킬문제
print(len(test_data))   # 38 테스트할문제
print(len(train_label)) # 112 훈련에 대한 답
print(len(test_label))  # 38 테스트의 답 

##연습) 훈련데이터로 공부시키고  테스트데이터로  예측 해 봅니다.
# clf = svm.SVC()
# clf.fit(train_data, train_label)

knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(train_data, train_label)

#4.8,3.1,1.6,.2,"Setosa"
userData = [[4.8,3.1,1.6,.2]]
result = knn.predict(userData)
print(result)

# 사용자한테 꽃잎의 길이, 꽃잎의 넓이, 꽃받침의 길이, 꽃받침의 넓이를
# 입력받아 붓꼿의 품종을 예측하는 웹어플리케이션 구현 해 봅니다.


# score = knn.score(test_data, test_label)
# print("정확도:",score)

# pre = clf.predict(test_data)

# print(pre[0])
# print(test_label.iloc[0])
# print(type(pre))
# print(type(test_label))


# n =  0
# for i in range(len(pre)):
#     if pre[i] == test_label.iloc[i]:
#         n= n +1
# print('정답수',n)


# print(pre)
# print(test_label)

# print(data[0])            #112          훈련시킬 문제
# print(len(data[1]))       #38         테스트할 문제
# print(data[2])            #112        훈련에 대한 답
# print(len(data[3]))       #38         테스할 답
# print(type(data))

# data = df.iloc[:,0:4]
# label = df.iloc[:,4]
#
# clf = svm.SVC()
# clf.fit(data, label)