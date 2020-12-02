import pandas as pd
import numpy as np

dat = pd.read_csv('datatest.txt', names =['rule','letter','line'], sep=' ')
dat['letter'] = dat['letter'].str.replace(':','')
dat['rule']
splitted = dat['rule'].str.split("-", n = 1, expand = True) 
dat['rstart'] = splitted[0]
dat['rend'] = splitted[1]
dat['rstart'] = dat['rstart'].astype(int)
dat['rend'] = dat['rend'].astype(int)



## part 1
for i in range(len(dat)):
    count = 0
    letter = dat['letter'][i]
    password = dat['line'][i]
    count = password.count(letter)
    if count >= int(dat['rstart'][i]) and count <= int(dat['rend'][i]):
        print(dat['line'][i])
        total.append(dat['line'][i])
print(len(total))

## part 2
total = []
dat['first'] = 0
dat['last'] = 0
for i in range(len(dat)):
    if dat['letter'][i] == dat['line'][i][(dat['rstart'][i]-1)]:
        dat['first'][i] = 1
    if dat['letter'][i] == dat['line'][i][(dat['rend'][i]-1)]:
        dat['last'][i] = 1

dat['total'] = dat['first'] + dat['last']
dat['total'].value_counts()
