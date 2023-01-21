import random
choice = int(input("Make your Choice: 0 for Rock, 1 for paper or 2 for scissor:   "))

computer = random.randint(0, 2)

print (computer)

if choice == 0  and computer == 2:
    print("You Win")
elif choice == 1 and computer == 0:
    print("You Win")
elif choice == 2 and computer == 1:
    print("You Win")
elif choice == 0 and computer == 1:
    print("You Suck")
elif choice == 1 and computer == 2:
    print("You Suck")
elif choice == 2 and computer == 0:
    print("You Suck")
else:
    print("DRAW")
