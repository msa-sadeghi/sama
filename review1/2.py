# print(2 ** 3)
# print(17 % 4)
# print(17 / 4)
# print(17 // 4)

a = 2
b = 3
c = b
b = a
a = c
print(a)
print(b)

a = 2
b = 3
a, b = b, a
print(a)
print(b)