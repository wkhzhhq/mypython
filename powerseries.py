x=float(input('Enter the value of x:'))
n=term=num=1
result=1.0
while term>=0.0000000001:
    term*=x/n
    result+=term
    n+=1
print 'No. of Times={} and Sum={:.10f}'.format(n,result)
