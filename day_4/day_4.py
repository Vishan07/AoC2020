import pandas as pd 
import numpy as np 
import re

with open("data.txt", "r") as myfile:
    data = myfile.read()

data = data.replace('\n\n','-newline-').replace('\n', ' ').replace('-newline-','\n')
data = data.splitlines()

to_check = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

## part 1
required_fields = 0
valid = 0
valid_data = []
for i in range(len(data)):          # iterate over passports
    required_fields = 0
    for j in range(len(to_check)):  # iterate over checkvalues
        if to_check[j] in data[i]:
            required_fields += 1
            if required_fields == 7:
                valid += 1
                valid_data.append(data[i]) # new dataset with only valid data
print('there are {} valid pasports'.format(valid))

## part 2
to_check = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
with open("datatest2.txt", "r") as myfile:
    data = myfile.read()

data = data.replace('\n\n','-newline-').replace('\n', ' ').replace('-newline-','\n')
data = data.splitlines()
data = valid_data

def datachecks(df):
    ecl = ['amb','blu','brn','gry','grn','hzl','oth']
    df['valid'] = 0
    for i in range(len(df)):
        # check if value has 4 digits, between 1920 and 2002
        if df['type'][i] == 'byr': 
            passed = re.search('^\d{4}$', df['value'][i])
            if passed and (int(df['value'][i]) >= 1920 and int(df['value'][i]) <= 2002):
                df['valid'][i] = 1

        # check if value has 4 digits, between 2010 and 2020
        if df['type'][i] == 'iyr': 
            passed = re.search('^\d{4}$', df['value'][i])
            if passed and (int(df['value'][i]) >= 2010 and int(df['value'][i]) <= 2020):
                df['valid'][i] = 1

        # check if value has 4 digits, between 2020 and 2030
        if df['type'][i] == 'eyr': 
            passed = re.search('^\d{4}$', df['value'][i])
            if passed and (int(df['value'][i]) >= 2020 and int(df['value'][i]) <= 2030):
                df['valid'][i] = 1

        # check if cm or inch, then  between 150 and 193 cm or between 59 and 76 in
        if df['type'][i] == 'hgt':
            if df['value'][i].endswith('cm') and (int(df['value'][i][:len(df['value'][i])-2]) > 149 and int(df['value'][i][:len(df['value'][i])-2]) < 194):
                print('true')
                df['valid'][i] = 1
            elif df['value'][i].endswith('in') and (int(df['value'][i][:len(df['value'][i])-2]) > 59 and int(df['value'][i][:len(df['value'][i])-2]) < 77):
                df['valid'][i] = 1
            else:
                df['valid'][i] = 0

        # check if a # followed by exactly six characters 0-9 or a-f.
        if df['type'][i] == 'hcl': 
            passed = re.search('^#([a-fA-F0-9]{6}|[a-fA-F0-9]{6})$', df['value'][i])
            if passed:
                df['valid'][i] = 1
       
        # exactly one of: amb blu brn gry grn hzl oth.            
        if df['type'][i] == 'ecl': 
            match = 0
            if df['value'][i] in ecl:
                match += 1
            if match == 1:
                df['valid'][i] = 1

        # a nine-digit number, including leading zeroes.          
        if df['type'][i] == 'pid': 
            passed = re.search('^[0-9]{9}$',df['value'][i])
            if passed:
                df['valid'][i] = 1

        if df['type'][i] == 'cid': 
            df['valid'][i] = 1

    return df

answer = 0
for j in range(len(data)):
    dataframe = pd.DataFrame(data[j].split(' '))[0].str.split(':', expand=True).rename(columns={0:'type',1:'value'})
    dataframe_incl_valid = datachecks(dataframe)
    if sum(dataframe_incl_valid['valid'] == 1) == len(dataframe_incl_valid):
        print(data[j])
        answer += 1
print(answer)
