fname = input('Enter a filename : ')
try:
    handle = open(fname)
except:
    print("Error, no such filename!")
    quit()

counts = {}
for line in handle:
    if not line.startswith('From') or len(line.split()) < 5:
        continue
    words = line.split()
    hour, minute, sec = words[5].split(':')
    counts[hour] = counts.get(hour, 0) + 1

#hour_list = list()
hour_list = sorted( [ (key, value) for (key, value) in counts.items() ] )

#for (key, value) in counts.items():
#    hour_list.append((key, value))

#hour_list.sort()
#print(hour_list)
for (key, value) in hour_list:
    print(key, value)
