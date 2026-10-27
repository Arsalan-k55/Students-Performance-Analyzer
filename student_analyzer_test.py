import unittest
from unittest.mock import patch
from Students_Performance_Analyzer import report,read_students

class TestStudentAnalyzer(unittest.TestCase):
    @patch("builtins.print")
    def test_report_with_no_students(self,mock_print):
        report([])

        mock_print.assert_called_with('No student records found')
    def test_readstudents_validation(self):
        students,invalid_records=read_students('test_students.csv')
        self.assertEqual(len(students),1)
        self.assertEqual(len(invalid_records),3)
        self.assertEqual(students[0],['Arsalan',95.0])
        self.assertIn(['Peter','abc','Invalid Marks'],invalid_records)
        self.assertIn(["Max", 120.0, "Marks out of range"], invalid_records)
        self.assertIn(["",75.0,'Empty Name'],invalid_records)
        self.assertEqual(students[0][1],95.0)
    def test_missing_columns(self):
        students,invalid_records=read_students('test_missing_columns.csv')
        self.assertEqual(len(students),0)
        self.assertEqual(len(invalid_records),2)
        self.assertIn(["Arsalan",'','Missing Columns'],invalid_records)
        self.assertIn(['57','','Missing Columns'],invalid_records)
    def test_missing_files(self):
        with self.assertRaises(FileNotFoundError):
            read_students('This file does not exist.csv')
    def test_empty_students(self):
        students,invalid_records=read_students('test_empty_students.csv')
        self.assertEqual(len(students),0)
        self.assertEqual(len(invalid_records),0)
    def test_header_only(self):
        students,invalid_records=read_students('Test_header_only.csv')
        self.assertEqual(len(students),0)
        self.assertEqual(len(invalid_records),0)
    @patch('builtins.print')
    def test_average_with_one_student(self,mock_print):
     
        students=[['Arsalan',85.0]]
        report(students)
        mock_print.assert_any_call('Average Marks: ',85.0)
    @patch("builtins.print")
    def test_average_for_two_students(self,mock_print):
        students=[['Arsalan',80.0],['Haris',90.0]]
        report(students)
        mock_print.assert_any_call('Average Marks: ',85.0)

if __name__ == "__main__":
    unittest.main()
    