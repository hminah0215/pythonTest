f = open('Data/member.txt', "w", encoding="utf-8")

list = []
list.append({"name":"이순신", "age":20})
list.append({"name":"유관순", "age":30})
list.append({"name":"김유신", "age":40})

print(list)
f.writelines(str(list))
print("ok")

# a = {"name":"이순신", "age":20}
# print(type(a))
# print(a)

# list = []
# list.append(10)
# list.append(20)
# list.append(30)
# list.append(40)
#
# print(list)