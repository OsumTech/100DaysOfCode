import os
from time import sleep
from turtle import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

biders = {}
repeat = "yes"

while repeat == "yes":
  name = input("Please Enter Your Name:  ")
  bid = input("Please Enter our Bid Amount: $")
  biders[name] = bid
  if name > bid:
    biders[name] = bid
  #print(biders)
  repeat = input("Is There any Other Bider? yes or no:  ")
  if repeat == "yes":
    os.system('cls')
  else:
    max_value = max(biders)
    print(f"The Winner is {max_value} with the bid of {biders[max_value]}" )
