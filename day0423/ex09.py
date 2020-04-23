import numpy as np
import matplotlib.pyplot as plt
import csv

f = open("day0423/student.csv", "r", encoding="UTF-8")
f.readline()
name =[]
kor = []
eng =[]

for line in csv.reader(f, delimiter="/"):
    name.append(line[0])
    kor.append(int(line[1]))
    eng.append(int(line[2]))

print(name)
print(kor)
print(eng)

bar_width = 0.4
plt.bar(range(len(kor)), kor, bar_width)
plt.bar(np.arange(len(kor))+bar_width, eng, bar_width)
plt.xticks(np.arange(len(kor)) +bar_width/2, name )
plt.show()

# print(name)
# print(kor)
# print(eng)