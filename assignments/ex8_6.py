num_list = list()
while True:
    num = input('Enter a number : ')
    try:
        num = float(num)
    except:
        if num == 'done': break
        print('Not a valid number!!')
        continue
    num_list.append(num)
print('Maximum :', max(num_list), '\nMinimum :', min(num_list))
