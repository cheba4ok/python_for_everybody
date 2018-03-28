fname = input('Enter a filename : ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        quit()
    print('Error, no such file!!!')
    quit()

count = 0
sum = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        start_pos = line.find(':')
        number = line[start_pos + 1:]
        sum += float(number)
        count += 1
        #print (line)
#print ('Number of lines = ', i, 'Sum of numbers = ', sum, 'Average = ', sum / i )
print ('The average spam confidence = ', sum / count )
