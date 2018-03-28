grep = input('Enter a command : ')

import re
#handle = open('mbox-short.txt')
handle = open('mbox.txt')

count = 0

for line in handle:
    line = line.rstrip()
    y = re.findall(grep, line)
    if len(y) > 0:
        #print(y)
        count += 1

print(count)
