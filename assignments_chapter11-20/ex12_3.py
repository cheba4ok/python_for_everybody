import urllib.request
fname = input("Enter a hostname : ")

try:
    handle = urllib.request.urlopen('http://' + fname)
except:
    print('Error, can\'t open a host')
    quit()
number = 0
for line in handle:
    content = line.decode().strip()
    for entry in content:
        number += 1
    if number > 3000 : break
    print(content)

print(number)
