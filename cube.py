import math

num = float(input("Enter a number: "))

cube = num ** 3
cube_root = num ** (1/3)
ln = math.log(num)
log2 = math.log2(num)
power6 = num ** 6

print("Cube =", cube)
print("Cube Root =", cube_root)
print("Natural Log =", ln)
print("Base 2 Log =", log2)
print("Power 6 =", power6)