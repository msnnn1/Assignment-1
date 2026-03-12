num = int(input("Enter a positive number: "))

if num < 0:
    print("Invalid input! Please enter a positive integer.")

else:
    fact = 1

    for i in range(1, num+1):
        fact = fact * i

    print("Factorial =", fact)