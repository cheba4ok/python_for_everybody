fname = input('Enter a filename : ')
try:
    handle = open(fname)
except:
    print('Error, no such filename!!!')
    quit()

counts = dict()
for line in handle:
    if not line.startswith('From') or len(line.split()) < 3:
        continue
    mail_list = line.split()
    counts[mail_list[2]] = counts.get(mail_list[2], 0) + 1
print(counts)
