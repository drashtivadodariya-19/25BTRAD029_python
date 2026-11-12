import random

while True:
    choice = input("\nRoll the dice? (yes/no): ")

    if choice.lower() == "yes":
        dice = random.randint(1, 6)
        print("Dice rolled:", dice)

    elif choice.lower() == "no":
        print("Game Over!")
        break

    else:
        print("Invalid choice!")
