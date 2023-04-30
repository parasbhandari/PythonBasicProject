import random

def guess_number(num):
    low=1
    high=num
    feedback=''
    while feedback!='c':
       guess=random.randint(low,high)
       feedback=input(f'Is {guess} is too low(l),too high(h or correct(c)?')
       if feedback=='l':
           low=guess+1
       elif feedback=='h':
           high=guess-1
        
    print("Yeah, computer choose right number")

guess_number(100)