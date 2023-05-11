# 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.


def expont_input(n, k):
    if (k == 1):
        return n
    if (k == 0):
        return 1
    if (k != 1):
        return (n * expont_input(n, k - 1))
        
n = int(input("Enter number: "))
k = int(input("Enter number to the extent: "))

print("Result manipulation: ", expont_input(n, k))