fname = input('Enter a filename : ')
try:
    fhand = open(fname)
except:
    print('Error, no such file!!')
    quit()
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        words = line.split()
        print(words[1])
        count += 1
print("There were", count, 'lines in the file with \'From\' as the first word')
