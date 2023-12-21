# constructor and instance variables

class Employee:

    def __init__(self, empId,empName,empAge):
        print("In Constructor")
        self.empId = empId
        self.empName = empName
        self.empAge = empAge
    

    def empInfo(self):
        print(self.empId)
        print(self.empName)
        print(self.empAge)

emp1 = Employee(13,"Vaibhav",22)
emp2 = Employee(14,"Vikee",22)
emp3 = Employee(15,"Dhiraj",23)
emp4 = Employee(16,"Yash",23)

emp1.empInfo()
emp2.empInfo()
emp3.empInfo()
emp4.empInfo()
