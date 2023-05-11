# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. использовать только + 1 - 1.

def summ(a, b):
    
    if b > 0:
        a += 1
        b -= 1
        return summ(a, b)
    return a
 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(summ(a, b))