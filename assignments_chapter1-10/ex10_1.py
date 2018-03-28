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

most_com = list()
for (key, value) in counts.items():
    most_com.append((value, key))

most_com.sort(reverse = True)

print(most_com[:5])
