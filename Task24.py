# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод — 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input("Введите кол -во кустов: "))
berries = [int(i) for i in input("Введите кол-во ягод на каждом кусту: ").split()]
max_berries = 0 
for i in range(n): 
    sum_berries = berries[i] + berries[(i + 1) % n] + berries[(i + 2) % n]  
    if sum_berries > max_berries:  
        max_berries = sum_berries  

print(max_berries)

# n = int(input())
# array = [int(i) for i in input().split()][:n]
# max_summa = 0
# for i in range(1, len(array) - 1):
#    if max_summa < array[i - 1] + array[i] + array[i + 1]:
#       max_summa = array[i - 1] + array[i] + array[i + 1]

# if max_summa < array[0] + array[1] + array[len(array) - 1]:
#    max_summa = array[0] + array[1] + array[len(array) - 1]
# if max_summa < array[0] + array[len(array) - 2] + array[len(array) - 1]:
#    max_summa = array[0] + array[len(array) - 2] + array[len(array) - 1]
# print(max_summa)