# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Введите кол-во элементов массива: "))
a = [int(i) for i in input("Введите числа массива: ").split()]
x = int(input("Введите число: "))
element = 0
for i in range(len(a)):
    if x - a[i] < x - element and x - a[i] > 0:
        element = a[i]
print(element)    

n = int(input("Введите кол-во элементов: "))
array = [int(i) for i in input("Введите значения массива: ").split()] 
x = int(input("Введите число, которое нужно подсчитать: "))
count = abs(x - array[0])
numbers = array[0]
for el in range(1, n):
    temp = abs(x - array[el])
    if count > temp:
        count = temp
        numbers = array[el]
print(numbers)
         