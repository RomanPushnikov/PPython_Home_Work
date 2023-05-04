# 16. Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводиt натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X


n = int(input("Enter how much numb: "))

num_list = list()
for i in range(n): 
    n = int(input('Enter number: ')) 
    num_list.append(n)
print(num_list)

x = int(input("Enter find numb: "))
count = 0

for i in range(len(num_list)):
    if num_list[i] == x:
        count += 1
print(count)