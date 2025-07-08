import random


cmp=random.choice(['rock','paper','scissorss'])
user=input('your choice')
print('cmpchoice:',cmp)

if cmp==user:
    print('tie')
elif user=='rock'and cmp=='scissors':
    print('win')
elif user=='paper'and cmp=='rock':
    print('win')
elif user=='scissors'and cmp=='paper':
    print('win')
else:
    print('you lose')