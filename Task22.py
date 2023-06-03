# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.


# n = int(input("Введите кол-во элементов 1-го множества: "))
# n = int(input("Введите кол-во элементов 2-го множества: "))
# m1 = set(int(i) for i in input("Введите числа 1-го множества: ").split())
# m2 = set(int(i) for i in input("Введите числа 2-го множества: ").split())
# print(sorted(m1 & m2))

mol = [int(x) for x in input().split()]  # 11 6
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()

a = [int(x) for x in input().split()][:n]
set_1 = set(a)
b = [int(x) for x in input().split()][:m]
set_2 = set(b)

lok = set_1 & set_2
kool = list(lok)
for i in range(len(kool)):
   for j in range(i + 1, len(kool)):
      if kool[i] > kool[i + 1]:
         temp = kool[i]
         kool[i] = kool[i + 1]
         kool[i + 1] = temp

for i in kool:
   print(i, end=' ')