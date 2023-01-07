#Write your code below this line 👇
def prime_checker(number):
    

    i = 1
    f = 0
    while i <= 9:
        d = number % i
        if d % i == 1:
            f = f+1
    
    if f > 1:
        print(f"{number} Is a Prime Number!")
    else:
        print(f"{number} Is not a Prime Number!")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
