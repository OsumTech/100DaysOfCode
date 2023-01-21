print("Welcome to Pizza Delivery")
size = input("What Size Pizza Do you want? S M L:  ")
pepperoni = input("Do you want pepperoni: ")
cheese = input("Do you want extra cheese? Y or N:  ")
bill = 0

if size == "s":
    bill = 15
    if pepperoni == "y":
        bill += 2
    if cheese == "y":
        bill += 1
        print(f"Your Bill Will be ${bill}")
    else:
        print(f"your bill will be ${bill}")
elif size == "m":
    bill = 20
    if pepperoni == "y":
        bill += 3
    if cheese == "y":
        bill += 1
        print(f"Your Bill Will be ${bill}")
    else:
        print(f"your bill will be ${bill}")
elif size == "l":
    bill = 25
    if pepperoni == "y":
        bill += 3
    if cheese == "y":
        bill += 1
        print(f"your bill will be ${bill}")
    else:
        print(f"your bill will be ${bill}")
