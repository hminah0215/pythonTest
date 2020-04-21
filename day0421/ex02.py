 # r 은 읽는것, w는 쓰는것 앞의 경로의 파일을 어쩌겠다~ 쓰는거임!
""" f = open('Data/song.txt','r',encoding="utf-8") 
text = f.readlines()

for line in text :
    print(line.strip()) #strip() 빈줄을 지워주세요.
f.close # 파일닫기 """

f = open('Data/info3.txt','w',encoding="utf-8")
age = 20
# f.write("홍길동\n")
# f.write(str(age)+"\n")
# f.write("서울시 마포구 신수동")

list = ['이순신\n',str(age)+"\n",'서울시 마포구 신수동\n']
f.writelines(list)
f.close
