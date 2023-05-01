s = int(input("Enter summ: s = "))
p = int(input("Enter multiplikation: p = "))

x1 = 0
x2 = 0
y1 = 0
y2 = 0
x = 0
y = 0
d = (s**2) - (4*p)

if d > 0:
    x1 += (s - (d**0.5))/2
    x2 += (s + (d**0.5))/2
    y1 += x2
#    y2 += s - x2
    print(x1, y1)
#    print(x2, y2)
elif d == 0:
    x += s/2
    y = x
    print(x, y)