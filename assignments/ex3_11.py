#ex3.11
'''
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
'''

score = input('Enter score: ')
try:
    score = float(score)
except:
    print("Bad input ")
    quit()

if (score > 1) or (score < 0):
    print('Bad score')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')
