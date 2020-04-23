import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib import font_manager, rc, colors, cm

f = open("day0423/gdp2019.csv", "r", encoding="UTF-8")
f.readline()
rank =[]
country = []
gdp =[]

for line in csv.reader(f):
    rank.append(int(line[0]))
    country.append(line[1])
    gdp.append(int(line[2]))

rank = rank[:10]
country = country[:10]
gdp = gdp[:10]

path = "C://Users//본인의 한글폰트가 설치되어있는곳 경로 적기//AppData//Local//Microsoft//Windows//Fonts//NanumGothic.ttf"
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font',family=font_name)

bar_width = 0.4
plt.bar(range(len(gdp)), gdp, bar_width, color=colors.TABLEAU_COLORS)
plt.xticks(np.arange(len(country)) +bar_width/2, country , rotation=45)
plt.title("2019 GDP TOP 10")
plt.show()