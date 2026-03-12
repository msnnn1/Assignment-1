start = int(input("Enter start of range: "))
end   = int(input("Enter end of range  : "))
result = []
count  = 0
total  = 0
for num in range(start, end + 1):
    if num % 9 == 0 and num % 6 != 0:
        result.append(num)
        count = count + 1
        total = total + num
print("\nNumbers divisible by 9 but NOT by 6:")
print(result)
print("\nCount of such numbers :", count)
print("Sum   of such numbers :", total)