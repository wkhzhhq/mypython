#!/usr/bin/python
import random
maxNumber=input('Please enter the maxium:')
minNumber=input('Please enter the minium:')
rightNumber=random.randrange(minNumber,maxNumber)
count=0
maxCount=5
while True:
    count+=1
    guessNumber=input('This is the count of {} of your guess,please enter your guess:'.format(count))
    maxCount-=1
    if maxCount<=0:
        print 'Sorry,you failed.'
        break
    if guessNumber==rightNumber:
        print 'Good!you guess count of {}'.format(count)
        break
    elif guessNumber>rightNumber:
        print 'Great!you have count of {} guess only,good luck!'.format(maxCount)
        continue
    elif guessNumber<rightNumber:
        print 'Little!you have count of {} guess only,good luck!'.format(maxCount)
        continue
