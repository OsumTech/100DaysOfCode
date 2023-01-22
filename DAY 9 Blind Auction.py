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

name = input("Please Enter Your Name:  ")
bid = input("Please Enter our Bid Amount: $")


biders[name] = bid



#os.system('cls')
