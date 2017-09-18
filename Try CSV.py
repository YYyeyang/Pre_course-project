import csv

with open('2016_ATUR_EVO.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
