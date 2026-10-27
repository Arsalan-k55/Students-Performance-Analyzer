import csv
with open('test_missing_columns.csv','w',newline="") as file:
    writer=csv.writer(file)
    writer.writerow(['Name'])
    writer.writerow(['Arsalan'])
    writer.writerow(['57'])