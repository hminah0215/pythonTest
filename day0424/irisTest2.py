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

# 훈련데이터로 공부시키고, 테스트 데이터로 예측해봅니다.
# 이렇게 해도 되고, sklearn neighbors를 사용해도 됨
''' clf = svm.SVC();
clf.fit(train_data, train_label)
a = clf.predict(test_data)
print(a) '''

knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(train_data,train_label)

r = knn.score(test_data, test_label)
print("정확도: ",r) # 정확도:  0.9473684210526315

