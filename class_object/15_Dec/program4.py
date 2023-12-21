
class College:

    dept = "Robotics And Automation"

    def __init__(self):
        self.studentName = "Vaibahv"
        self.studentRollNo = 50
        self.studentZPRN = 1207516

    def student_details(self):
        print(self.studentName)
        print(self.studentRollNo)
        print(self.studentZPRN)
        print(self.dept)

std_Details = College()

print(std_Details.studentName)
print(std_Details.dept)

College.dept = "R&A"

std_Details.student_details()
