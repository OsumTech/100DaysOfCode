#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    while is_prime == True:

      for i in range(2,number-1):
        factor = number % i

        if factor == 0:
            is_prime = False
            print(f"{number} is not a Prime Number!")

    print(print(f"{number} is a Prime Number!"))
        



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
