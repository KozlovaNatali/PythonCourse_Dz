# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

num = int(input("Введите трёхзначное число: "))
if num < 0:
    num = -num
if num > 99 and num < 1000:
    firstdigit = num // 100
    seconddigit = num % 100 // 10
    thirddigit = num % 10
    print(firstdigit + seconddigit + thirddigit)
else:
    print('Вы ввели не трёхзначное число')    


