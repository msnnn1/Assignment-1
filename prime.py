start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0
sum = 0

for n in range(start, end+1):
    if n > 1:
        prime = True

        for i in range(2, n):
            if n % i == 0:
                prime = False

        if prime:
            print(n)
            count = count + 1
            sum = sum + n

print("Total prime numbers =", count)
print("Sum of prime numbers =", sum)