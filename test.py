import csv

with open('Avg_age_processed.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



