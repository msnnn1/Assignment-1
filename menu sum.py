pos_sum = 0
neg_sum = 0

choice = "y"

while choice == "y":
    num = int(input("Enter a number: "))

    if num > 0:
        pos_sum = pos_sum + num
    elif num < 0:
        neg_sum = neg_sum + num

    choice = input("Do you want to enter another number? (y/n): ")

print("Sum of positive numbers =", pos_sum)
print("Sum of negative numbers =", neg_sum)