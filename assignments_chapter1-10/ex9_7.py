fname = input('Enter a filename : ')
try:
    handle = open(fname)
except:
    print('Error, no such filename!')
    quit()

counts = {}
for line in handle:
    if not line.startswith('From'):
        continue
    email_list = line.split()
    domen = email_list[1].split('@')
    counts[domen[1]] = counts.get(domen[1], 0) + 1
print(counts)
