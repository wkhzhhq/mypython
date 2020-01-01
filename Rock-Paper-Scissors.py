#/usr/bin/python
import random
a=[1,2,3]
scort=0
for count in range(1,4):
    computerchoice=random.choice(a)
    yourchoice=input('The count of {} battle,please enter your choice(enter 1 for rock,2 for scissors,3 for paper):'.format(count))
    result=yourchoice-computerchoice
    if result==-1 or result==2:
        scort+=1
    elif result==0:
        pass
    else:
        scort-=1
if scort>0:
    print 'Your scort is {} ,you win!'.format(scort)
elif scort==0:
    print 'Your scort is {},draw!'.format(scort)
else:
    print 'Your scort is {},you failed!'.format(scort)

