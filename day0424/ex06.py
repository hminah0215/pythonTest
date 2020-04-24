from sklearn import svm

# 수집한 데이터가 이렇게 있다고 가정! 두개는 feature, 한개는 답으로 본다
xor_data= [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

data = []
label = []

for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]

    data.append([p,q])
    label.append(r)

# print(data)     #문제 [[0, 0], [0, 1], [1, 0], [1, 1]]
# print(label)    #답   [0, 1, 1, 0]

# 공부시키는 도구, fit 공부해봐 (문제, 답)
clf = svm.SVC();
clf.fit(data,label)

# 공부했으면 알아맞춰봐 
pre = clf.predict(data)
print(pre)      # [0 1 1 0] 답 다 잘 맞춤, 데이터가 몇건 안되니까 ㅎ 



