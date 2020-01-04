sum=0
args=input("Please input the numbers(use ',' seperate the element):")
for i in args:
    number=float(i)
    sum+=number
average=sum/len(args)
print 'The number of input is {},the sum of input is {}.'.format(len(args),sum)
print 'Average of input is {:.2f}'.format(average)

