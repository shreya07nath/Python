import random

def game(comp,you):
    if comp == you:
        return None
    if comp == 'r':
        if you=='p':
            return True
        elif you =='s':
            return False
    if comp == 'p':
        if you=='r':
            return True
        elif you =='s':
            return False
    if comp == 's':
        if you =='p':
            return True
        elif you =='r':
            return False


num = random.randint(1,3)
print("Computer is choosing rock(r), paper(p), scissor(s)")
if num == 1:
    comp= 'r'
elif num == 2:
    comp= 'p'
elif num == 3:
    comp= 's'

you = input("What is your choice rock(r), paper(p), scissor(s): ")
print(f"computer chose {comp}")
print(f"you chose {you}")
win=game(comp,you)
if win == None:
    print("It's a Tie!")
elif win == True:
    print("You Won!!")
else:
    print("You Lost")
