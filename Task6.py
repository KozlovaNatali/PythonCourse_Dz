# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
b = int(input("Введите номер билета: "))
if b > 100000 and b < 1000000:
   first_three_digits = b // 1000
   first_digit1 = first_three_digits // 100
   second_digit1 = first_three_digits % 100 // 10
   third_digit1 = first_three_digits % 10
   sum1 = first_digit1 + second_digit1 + third_digit1
   last_three_digits = b % 1000
   first_digit2 = last_three_digits // 100
   second_digit2 = last_three_digits % 100 // 10
   third_digit2 = last_three_digits % 10
   sum2 = first_digit2 + second_digit2 + third_digit2
if sum1 == sum2:
   print('Yes')   
else:
   print('No')   
   