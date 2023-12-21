# class variables or static variables

class Company:

    compName = "Bostan Dynamics"

    def __init__(self):
        print("In Instructor")
        self.empId = 14
        self.empName = "Vaibhav"
        self.empAge = 22

    def compInfo(self):
        print(self.empId)
        print(self.empName)
        print(Company.compName)
        print(self.empAge)

emp1 = Company()

emp1.compInfo()

emp2 = Company()

emp1.compInfo()
emp2.compInfo()

Company.compName = "The Construct"

emp1.compInfo()
emp2.compInfo()
