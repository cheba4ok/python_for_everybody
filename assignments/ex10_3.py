### letter frequency
import string

fname = input('Enter a filename : ')
try:
    handle = open(fname)
except:
    print('Error, no such filename!!')
    quit()
### added to string.punctuation method numbers, cause we need only letters
string.punctuation += '0123456789'

counts = {}
sum = 0
for line in handle:
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            counts[letter] = counts.get(letter, 0) + 1
            sum += 1

letter_list = list()

for (key, value) in counts.items():
    letter_list.append((value / sum, key))

letter_list.sort(reverse = True)
#print(counts)
#print(letter_list)
for (key, value) in letter_list[:10]:
    print(value, key)
