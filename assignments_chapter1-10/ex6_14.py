str = ' X-DSPAM-Confidence: 0.8475  '

start_pos = str.find(':')
new_str = str[start_pos + 1:]
print(float(new_str))

## how not to do : 
## print(float(str[str.find(':') + 1:]))
