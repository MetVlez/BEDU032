import csv
# CONSTANT
FILENAME = 'employess.csv'
with open(FILENAME, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row.get('Salary'))