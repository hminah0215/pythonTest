import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm

df = pd.read_csv("day0424/iris.csv")
# print(df) # [150 rows x 5 columns]
# print(type(df))   # <class 'pandas.core.frame.DataFrame'>

# print(df[0,0]) 이렇게 하는건 불법! 아래처럼 iloc 함수를 통해서 접근해야한다.
# print(df.iloc[0,0])

# 위는 문제 뽑아옴, 아래는 답 뽑아옴 
data = df.iloc[:,0:4]   #  : , ~~행은 생략하면 전부다~
label = df.iloc[:,4]

# print(type(data))   #<class 'pandas.core.frame.DataFrame'>
# print(type(label))  #<class 'pandas.core.series.Series'>

clf = svm.SVC();
clf.fit(data,label)

# 4.7,3.2,1.6,.2,"Setosa" 데이터 하나만 주고 알아맞춰보라고 할것!
newData = [[4.7,3.2,1.6,.2]]
a = clf.predict(newData)
print(a)    # ValueError: Expected 2D array, got 1D array instead: 그러니 newData를 이차원배열꼴로 해줘야 결과가 나온다.

# r = clf.predict(data)
# print(r)