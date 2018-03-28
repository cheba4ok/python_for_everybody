#ex3.11
def computepay():
    hours = input('Enter hours: ')
    rate = input('Enter rate: ')
    try:
        hours = float(hours)
        rate = float(rate)
    except:
        return ('Error, please numeric input')
    if hours > 40:
        ex_hours = (hours - 40) * rate * 1.5
        return (ex_hours + (40 * rate))
    else:
        return (hours * rate)

print (computepay())

def computegrade(score):
    #score = input('Enter score: ')
    try:
        score = float(score)
    except:
        return ("Bad input ")
        #quit()

    if (score > 1) or (score < 0):
        return('Bad score')
    elif score >= 0.9:
        return('A')
    elif score >= 0.8:
        return('B')
    elif score >= 0.7:
        return('C')
    elif score >= 0.6:
        return('D')
    else:
        return('F')

print (computegrade(input('Enter score : ')))
