n=int(input('Enter the number of students:'))
data={}
subjects=['Physics','Maths','History']
for i in range(n):
    name=raw_input('Enter the name of student:')
    mask=[]
    for x in subjects:
        mask.append(float(input('Enter the mark of {}:'.format(x))))
    data[name]=mask
for a,b in data.items():
    total=sum(b)
    print "{}'s total marks is {}.".format(a,total)
    if total<120:
        print x,'failed!'
    else:
        print x,'passed!'

