fname = input('Enter a filename : ')
try:
    fhand = open(fname)
except:
    print('Error, no such file!!!')
    quit()
    
for line in fhand:
    line = line.strip().upper()
    print(line)
