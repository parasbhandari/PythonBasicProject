import random
def play():
    me=input("Enter 'r' for rock, 'p' of paper and 's' for scissor ")
    pc= random.choice(['r','p','s'])
    if me==pc:
        print("Game tie")
    elif check_win(me,pc):
        print("You won")
    else:
        print("You lost")
    print("Your choice {}".format(me))
    print("PC choice is {}".format(pc))
    
#  r>s,s>p,p>r
def check_win(me,pc):
    if (me=='r' and pc=='s') or (me=='s' and pc=='p') or (me=='p' and pc=='r'):
        return True
        

play()