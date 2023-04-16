# Найдите сумму цифр трехзначного числа.

n = int(input('Enter number ***: '))

print(f"Summ numbers = {n//100 + n//10%10 + n%10}")