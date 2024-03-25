#Задание 1.
#создать 2 массива в 1 млн случайных значений
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import time
#Создание стандартных списков
random_list1 = [randint(-1000000, 1000000) for i in range(1000000)]
random_list2 = [randint(-1000000, 1000000) for i in range(1000000)]

#random_list3 = []
#Начало замера времени
t_start = time.perf_counter()

random_list3 = list(map(lambda x, y: x*y, random_list1, random_list2))

#for i in range(0, len(random_list1)):
#    random_list3.append(random_list1[i] * random_list2[i])
time.sleep(1)
#Конец замера времени
all_time = time.perf_counter() - t_start

#Создание массива NumPy
rand_listik1 = np.random.randint(-1000000, 1000000, 1000000)
rand_listik2 = np.random.randint(-1000000, 1000000, 1000000)
#Начало замера времени
t_start1 = time.perf_counter()

rand_listik3 = np.multiply(rand_listik1, rand_listik2)

time.sleep(1)
#Конец замера времени
all_time1 = time.perf_counter() - t_start1
#Разница времени
all_time2 =  all_time -  all_time1
print('Разница во времени: ',  all_time2)




#Задание 2.
#Вариант 5 data1.cvs
import pandas as pd
import seaborn as sns

data = pd.read_csv("data1.csv", sep = ";", encoding='latin-1')

x_data = data.iloc[:, 0]
y1_data = data.iloc[:, 3]
y2_data = data.iloc[:, 6]

plt.figure(figsize=(10, 6))
plt.plot(x_data, y1_data, label = 'График 1')
plt.plot(x_data, y2_data, label = 'График 2', linestyle='--')
plt.xlabel('Время')
plt.ylabel('ось Y')
plt.title('График данных из файла')
plt.legend()
plt.show()

#Построение графика корреляции
ctolbsi = data.columns[[0, 3, 6]]
ctols = data[ctolbsi]
correlation = ctols.corr()

plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('График корреляции')
plt.show()




#Задание 3.
#x∈(-п;п); y=sin(x)cos(x); z=sin(x)
x = np.linspace(-np.pi, np.pi,100)
y = np.sin(x) * np.cos(x)
z = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
