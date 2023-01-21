print("Welcome to Roller Coster Ride!")
height = int(input("Please Enter Your Height in cms:  "))

if height >=120:
    print("Cogratulations, You can ride roller coster!!!")
    age = int(input("Please Enter Your Age  "))
    if age <12:
        print("Your Bill will be $5")
        if age >18:
            print("You Bill will be $12")
    else:
        print("Yor Bill Will Be $7")
else:
    print("Sorry, You have to grow taller to ride the Roller Coster")
