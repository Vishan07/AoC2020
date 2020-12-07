import pandas as pd
import numpy as np 
from csv import reader
from collections import Counter

## part 1 
with open("data.txt", "r") as myfile:
    data = myfile.read()

data = data.split('\n\n')
data = [data[i].replace('\n','') for i in range(len(data))]

total_sum = 0
for i in range(len(data)):
    count = len(set(data[i]))
    total_sum = total_sum + count
print(total_sum)

## part 2
with open("data.txt", "r") as file:
    data = file.read().split("\n\n")
    data = [i.splitlines() for i in data]

total_sum = 0
for i in range(len(data)): # iterate over groups
    total_set = set()
    for j in range(len(data[i])): # iterate over individuals in groups
        if len(data[i]) == 1:
            som = len(data[i][j])
            total_sum = total_sum + som
            #print(data[i])
            #print(som)
        else:
            try:
                total_set = set(data[i][j]).intersection(set(data[i][j+1]))
                som = len(total_set)
            except:
                total_sum = total_sum + som
print(total_sum)

## correct
print(sum([len(set.intersection(*[set(j) for j in i.split()])) for i in open('data.txt').read().split('\n\n')]))
