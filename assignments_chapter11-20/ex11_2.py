import re

#handle = open('mbox-short.txt')
handle = open('mbox.txt')

sum = 0
count = 0

for line in handle:
    line = line.rstrip()
    y = re.findall('New Revision:.* ([0-9.]+)', line)
    if len(y) > 0:
        #print(y)
        sum += float(y[0])
        count += 1
print('Average of numbers :', sum / count)
