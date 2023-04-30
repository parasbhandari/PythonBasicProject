import random

def guess_number(num):
     x=random.randint(1,num+1)
     choose=0
     while choose!=x:
          choose=int(input(f'Guess the number between {1} and {num}: '))
          if choose>x:
               print("Number is too high")
          elif choose<x:
               print("Number is too low")
          else:
               print("Yeh, you choose right number")

    
guess_number(100)
