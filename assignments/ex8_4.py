fhand = open('romeo.txt')
words_list = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in words_list:
            words_list.append(word)
words_list.sort()
print(words_list)
