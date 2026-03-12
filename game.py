import random

number = random.randint(1,50)

for i in range(7):
    guess = int(input("Guess the number: "))

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct!")
        break

else:
    print("Better luck next time!")