n = int(input('введите кол-во монет: '))
count_min = 0
count_max = 0

for i in range(1, n + 1):
    x = int(input(f"сторона {i}: "))
    if x == 0:
        count_min += 1
    elif x == 1:
        count_max += 1
if count_min <= count_max:
    print (f"Нужно перевернуть {count_min} раз")
else:
    print (f"Нужно перевернуть {count_max} раз")