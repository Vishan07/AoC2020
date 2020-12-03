import pandas as pd
import numpy as np

data = pd.read_csv('data.txt', header=None)
data = data[0].str.split('', expand=True)
data.dropna(axis=1, inplace=True)
data = pd.concat([data]*100, axis=1,ignore_index=True)

## part 1
def path(r,d):
    ri, di = r,d
    path = [data[0][0]]
    for i in range(len(data)):
        position = data[r][d]
        #print(r,d)
        path.append(position)
        r = r + ri
        d = d + di
        if d > len(data)-1:
            #print(path)
            break
    return path.count('#')
path(3,1)

## part 2
v1 = path(1,1)
v2 = path(3,1)
v3 = path(5,1)
v4 = path(7,1)
v5 = path(1,2)

output = v1*v2*v3*v4*v5
print(output)