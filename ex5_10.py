#ex5_10
sum = 0
count = 0
num = None
max = None
min = None
while True:
    num = (input('Enter a number: '))
    if num == 'done':
        break
    try:
        num = float(num)
    except:
        print('Bad data')
        continue
    if max is None or num > max:
        max = num
    if min is None or num < min:
        min = num
    count += 1
    sum += num

print('Sum of numbers = ', sum, 'Count of number = ', count, 'Average = ', sum/count)
print('Max = ', max, 'Min = ', min)
#print('Sum of numbers = ', sum)
#print('Sum of numbers = ', sum)
###test for github
