import pandas as pd
import numpy as np

def read_data(input):
    data = pd.read_csv(input, header=None)
    return data

## part 1
data = read_data('data.txt')[0]
seat_ID_overview = []
seats_overview = []
plane_rows_start = list(range(0,128))
plane_seats_start = list(range(0,8))
i=0
for i in range(len(data)):
    code = data[i]
    plane_rows = plane_rows_start
    seat_rows = plane_seats_start
    for j in range(len(code)):
        if code[j] == 'F':
            # take first half of list
            middle_index = len(plane_rows)//2
            plane_rows = plane_rows[:middle_index]
            #print('F. Middle_index:{}'.format(middle_index))
            #print(plane_rows)
        elif code[j] == 'B':
            # take second half of list
            middle_index = len(plane_rows)//2
            plane_rows = plane_rows[middle_index:]
            #print('B. Middle_index:{}'.format(middle_index))
            #print(plane_rows)
        elif code[j] == 'L':
            # take second half of list
            middle_index = len(seat_rows)//2
            seat_rows = seat_rows[:middle_index]
            #print('L. Middle_index:{}'.format(middle_index))
            #print(seat_rows)        
        elif code[j] == 'R':
            # take second half of list
            middle_index = len(seat_rows)//2
            seat_rows = seat_rows[middle_index:]
            #print('R. Middle_index:{}'.format(middle_index))
            #print(seat_rows)        
        
        if len(plane_rows) == 1 and len(seat_rows) == 1:
            seat_ID = (int(plane_rows[0]) * 8) + int(seat_rows[0])
            seats_overview.append([int(plane_rows[0]), int(seat_rows[0]),seat_ID])
            print('row: {}, seat: {}, seatID = {}'.format(plane_rows, seat_rows, seat_ID))
            seat_ID_overview.append(seat_ID)
#print(seat_ID_overview)
print(max(seat_ID_overview))

## part 2

# create overview of all occupied seats
seats_overview_df = pd.DataFrame(seats_overview, columns=['row','seat','seat_ID'])
# add column with unique row+seat
seats_overview_df['row+seat'] = 0
for i in range(len(seats_overview_df)):
    seats_overview_df['row+seat'][i] = int(str(seats_overview_df['row'][i])+str(seats_overview_df['seat'][i]))

# generate overview of all potential rows and seats and seatIDs
all_seats = []
for i in range(len(plane_rows_start)):
    for j in range(len(plane_seats_start)):
        seat = [i,j]
        all_seats.append(seat)
print(all_seats)

all_seats_df = pd.DataFrame(all_seats, columns=['row','seat'])
all_seats_df['seat_ID'] = 0
for i in range(len(all_seats_df)):
    all_seats_df['seat_ID'][i] = (int(all_seats_df['row'][i]) * 8) + int(all_seats_df['seat'][i])

# find which seat_IDs are not present in seat_ID_overview
missing_seats = all_seats_df.loc[~all_seats_df['seat_ID'].isin(seats_overview_df['seat_ID'])]