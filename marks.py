m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))
m6 = float(input("Enter marks of subject 6: "))

total = m1 + m2 + m3 + m4 + m5 + m6
average = total / 6
percentage = (total / 600) * 100

print("Total =", total)
print("Average =", average)
print("Percentage =", percentage)

if percentage >= 85:
    print("Grade: Distinction")
elif percentage >= 70:
    print("Grade: First Division")
elif percentage >= 55:
    print("Grade: Second Division")
elif percentage >= 45:
    print("Grade: Third Division")
else:
    print("Grade: Fail")