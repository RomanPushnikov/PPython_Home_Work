n = int(input("Enter how much numb: "))

num_list = list()
for i in range(n): 
    n = int(input('Enter number: ')) 
    num_list.append(n)
print(num_list)

x = int(input("Enter numb  X: "))

raznost = abs(x - num_list[0])
b = 0
i = 0

while i < len(num_list):
    if abs(x - num_list[i]) <= raznost:
        raznost = abs(x - num_list[i])
        b = i
    i += 1

print(num_list)
print(f"Closet:  {num_list[b]}")
print(b)