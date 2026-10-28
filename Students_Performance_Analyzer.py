import csv
def read_students(filename="students.csv"):
  students=[]
  invalid_records=[]

   #----Read Student's Records-------:
  with open(filename,'r',newline="") as file:
      reader=csv.reader(file)
      header=next(reader,None)
      if header is None:
         return students,invalid_records
      for row in reader:
       
        #---Check whether the row has enough columns----:
        if len(row)<2:
           print('Skipping invalid row: ',row)
           name=row[0].strip() if len(row)> 0 else ""
           marks_text=row[1].strip() if len(row)> 1 else ""
           invalid_records.append([name,marks_text,'Missing Columns'])
           continue
        name=row[0].strip()
        #Check whether marks can be converted to a number----:
        raw_marks=row[1].strip()
        try:
         marks=float(row[1])
        except ValueError:
           print('Invalid marks for: ',name,'-Skipping row...')
           invalid_records.append([name,raw_marks,'Invalid Marks'])
           continue
        #----Check whether a name is empty----:
        if not name:
           print('Skipping row with empty name')
           invalid_records.append([name,marks,'Empty Name'])
           continue
        #----Validate the marks----:
        if marks<0 or marks>100:
           print('Invalid Marks range for: ',name,'-Skipping row')
           invalid_records.append([name,marks,'Marks out of range'])
           continue
        students.append([name,marks])

  return students,invalid_records



def report(students):
    
    passed=0
    failed=0

#----Check whether the file has student's records-----:
    if len(students)>0:
    #----Students Passed/Failed counter-------:
       for student in students:
           marks=student[1]
           if marks>=50:
                passed+=1
           else:
                failed+=1

    #----Calculate Average Marks------:
       total_marks=sum(student[1] for student in students)
       average=total_marks/len(students)
    #----Calculate the Pass Percentage----:
       pass_percentage=passed/len(students)*100
    #----Calculate the Fail Percentage----:
       fail_percentage=failed/len(students)*100
    #----Find the highest and lowest scorers----:
       top_student=max(students,key=lambda students:students[1])
       lowest_student=min(students,key=lambda students:students[1])

#----Display the report----:
       print('Total Students: :',len(students))
       print('Average Marks: ',round(average,2))
       print('Pass Percentage: ',pass_percentage)
       print('Fail Percentage: ',fail_percentage)
       print('Top Student: ',top_student[0])
       print('Highest Marks: ',top_student[1])
       print('Lowest-Scorer Student: ',lowest_student[0])
       print('Lowest Marks: ',lowest_student[1])
       print(f'Students Passed: {passed}')
       print(f'Students Failed: {failed}')
#----Display Individual Student Results----:
       print('================================')
       print('================================')
       print('Individual Student Results')
       for student in students:
            name=student[0]
            marks=student[1]
            if marks>=50:
                status='Pass'
            else:
                status='Fail'
            print(name,'| Marks: ',marks,'| Status: ',status)
    else:
     print('No student records found') 
     
def save_invalid_records(invalid_records):
   with open('Invalid_records.csv','w',newline="") as file:    
       writer=csv.writer(file)
       writer.writerow(['Name', 'Marks', 'Reason'])
       writer.writerows(invalid_records)
   print('Invalid Records Saved: ',len(invalid_records))

def main():
   
   students,invalid_records=read_students()
   print(f"Total Valid records: {len(students)}")
   print(f"Total Invalid records: {len(invalid_records)}")
   report(students)
   save_invalid_records(invalid_records)
if __name__=="__main__":
      main()

#----Students Performance Analyzer-------