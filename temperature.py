fahrenheit=0
print 'Fahrenheit Celsius'
while fahrenheit<=250:
    celsius=(fahrenheit-32)/1.8 #temprature converse
    print '{:5d} {:7.2f}'.format(fahrenheit,celsius)
    fahrenheit+=25

