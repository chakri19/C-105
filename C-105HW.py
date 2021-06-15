import csv
import math

with open("data2.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def Mean(data):
    m = len(data)
    total = 0
    for x in data:
        total+=int(x)
    mean = total/m
    return mean

squareList = []
for number in data:
    subtractNum = int(number) - Mean(data)
    squareNum = subtractNum ** 2 
    squareList.append(squareNum)

sum = 0
for n in squareList:
    sum += n

divideNum = sum/(len(data) - 1)
final = math.sqrt(divideNum)
print(final)