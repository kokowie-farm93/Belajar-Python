# // *10 // 3 = 3 
# %  *10 % 3 = 1

a = 10
b = 3
print(a // b) # 10 // 3 = 3
print(a % b) # 10 % 3 = 1
print(a ** b) # 10^3 = 1000
print(a * b) # 10*3 = 30
print(a / b) # 10/3 = 3.3333333333333335
print(a + b) # 10+3 = 13
print(a - b) # 10-3 = 7

print("--------")
#compound assignment operator
a = 10
a += 3 # a = a + 3
print(a) # 13
a -= 2 # a = a - 2
print(a) # 11
a *= 2 # a = a * 2
print(a) # 22
a /= 2 # a = a / 2
print(a) # 11.0
a %= 3 # a = a % 3
print(a) # 2.0
a **= 3 # a = a ** 3
print(a) # 8.0
a //= 2 # a = a // 2
print(a) # 4.0