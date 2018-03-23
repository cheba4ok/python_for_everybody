#ex3.11
hours = input('Enter hours: ')
rate = input('Enter rate: ')
try:
    hours = int(hours)
    rate = int(rate)
except:
    hours = -1
    rate = -1
#print (hours, rate)
if (hours or rate) < 0:
    print ('Error, please numeric input')
else:
    if hours > 40:
        print ((hours - 40) * rate * 1.5 + (40 * rate))
    else:
        print (hours * rate)
