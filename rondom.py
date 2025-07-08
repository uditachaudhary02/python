import random
roll=random.randint(1,6)
guess=int(input('guess dice roll:\n'))
if guess== roll:
    print("cmp rolled a"+ str(roll))
else:
    print("wrong")