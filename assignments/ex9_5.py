fname = input('Enter a filename : ')
try:
    handle = open(fname)
except:
    print('Error, no such filename!')
    quit()
counts = dict()

for line in handle:
    if line.startswith('From:'):
        email_list = line.split()
        counts[email_list[1]] = counts.get(email_list[1], 0) + 1
print(counts)

### ex9_6, finds who has the most messages and print how many messages the person has
print('\n\n', max(counts), max(counts.values()))
