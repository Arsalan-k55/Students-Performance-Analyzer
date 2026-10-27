import csv
with open ('students.csv','w',newline="") as file:
    writer=csv.writer(file)
    writer.writerow(['Name','Marks'])
    writer.writerow(['Arsalan','95'])
    writer.writerow(['Zamin','98'])
    writer.writerow(['Haris','98.5'])
    writer.writerow(['Max','120'])
    writer.writerow(['Alex'])
    writer.writerow(["",'100'])
    writer.writerow(['Peter','abc'])