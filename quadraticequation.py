import math
a=int(input('Enter value of a:'))
b=int(input('Enter value of b:'))
c=int(input('Enter value of c:'))
d=b*b-4*a*c
if d<0:
    print 'ROOTS are imaginary'
elif d==0:
    root=-b/(2*a)
    print 'root={}'.format(root)
else:
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    print 'root1={}'.format(root1)
    print 'root2={}'.format(root2)
    
