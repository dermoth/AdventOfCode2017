#!/usr/bin/env python3

data = []
with open('input.txt', 'r') as f:
    for line in f:
        data.append(line.split())

#data = [
#    ['5', '9', '2', '8'],
#    ['9', '4', '7', '3'],
#    ['3', '8', '6', '5'],
#]    

res = 0
for line in data:
    #found  = None
    for i in range(0, len(line)):
        cell1 = line[i]
        for cell2 in line[i:]:
            if cell1 == cell2:
                continue
            elif int(cell1) < int(cell2):
                val1 = int(cell2)
                val2 = int(cell1)
            elif int(cell1) > int(cell2):
                val1 = int(cell1)
                val2 = int(cell2)
            else:
                raise Exception(cell1,cell2)
            if val1 % val2 == 0:
                res += int(val1 / val2)

print(res)

