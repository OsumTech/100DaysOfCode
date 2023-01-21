your_name = input("What is your name? \n")
her_name  = input("What is her name?  \n")

your_name = your_name.lower()
her_name = her_name.lower()
final_name = (your_name + her_name)


t = final_name.count("t")
r = final_name.count("r")
u = final_name.count("u")
e = final_name.count("e")
l = final_name.count("l")
o = final_name.count("o")
v = final_name.count("v")
e = final_name.count("e")

love = (t + r + u + e + l + o + v + e)
print(love)

if love < 10 or love > 90:
    print(f"your score is {love} You guys go like coke  mentos together")
elif love > 40 & love < 50:
    print(f"your score is {love} You guys are fine together")
else:
    print(f"your score is {love}.")    
