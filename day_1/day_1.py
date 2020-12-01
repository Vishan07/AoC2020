import pandas as pd
import numpy as np

dat = pd.read_csv('data.txt', header=None)

sum = 0
while sum != 2020:
    for i in range(len(dat)):
        sum = (i + (i+1))
    print(sum)
    