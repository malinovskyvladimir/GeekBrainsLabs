# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа
###

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу используя только две переменные

# n1 = int(input("Define 1st int variable:"))
# n2 = int(input("Define 2nd int variable:"))
# print(n1)
# print(n2)
# n1 = n1 ^ n2
# n2 = n1 ^ n2
# n1 = n1 ^ n2
# print(n1)
# print(n2)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функицй sqrt() молудя math
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
print(" input values a, b, c for expression ax2 + bx + c = 0")
a = float(input("Input a = "))
b = float(input("Input b = "))
c = float(input("Input c = "))
# Discriminant definition expression
D = b ** 2 - 4 * a * c
print(D)
if D < 0:
    print("there are no roots")
elif D == 0:
    x = -b / 2 * a
    print("There is only one root, value = " + str(x))
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("There are 2 roots, value1 = " + str(x1) + " value2 = " + str(x2))
