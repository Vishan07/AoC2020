import pandas as pd
import numpy as np

dat = pd.read_csv('data.txt', header=None)
dat = dat[0].tolist()

## part 1
for i in range(len(dat)-1):
    for j in range(len(dat)-1):
        sum = dat[i] + dat[j]
        if sum == 2020:
            print (dat[i] * dat[j])

## part 2
for i in range(len(dat)-1):
    for j in range(len(dat)-1):
        for z in range(len(dat)-1):
            sum = dat[i] + dat[j] + dat[z]
            if sum == 2020:
                print (dat[i] * dat[j] * dat[z])