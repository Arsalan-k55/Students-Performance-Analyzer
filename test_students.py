import csv
with open("test_students.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(['Name','Marks'])
    writer.writerow(['Arsalan','95'])
    writer.writerow(["Max","120"])
    writer.writerow(["Peter","abc"])
    writer.writerow(["","75"])
