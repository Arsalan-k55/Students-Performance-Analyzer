import csv
with open('Test_header_only.csv','w',newline="") as file:
    writer=csv.writer(file)
    writer.writerow(['Name','Marks'])