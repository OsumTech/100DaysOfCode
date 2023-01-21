print("Welcome to Roller Coster Ride!")
height = int(input("Please Enter Your Height in cms:  "))
picture = input("Would you like to take picture?  Y or N:  ")
bill = 0

if height >=120:
    print("Cogratulations, You can ride roller coster!!!")
    age = int(input("Please Enter Your Age  "))
    if age <12:
        bill = 5
    elif age <= 18:
            bill = 7
    elif age >= 45 and age <=55:
            print("We got your back you can ride for free")
    else:
        bill = 12
    if picture == "Y":
        bill = bill + 3
        print(f"Your Bill will be ${bill}")
    else:
        print(f"Your bill will be ${bill}")
else:
    print("Sorry, You have to grow taller to ride the Roller Coster")
