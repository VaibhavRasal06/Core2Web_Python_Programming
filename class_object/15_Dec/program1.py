class Employee:

    Comapany = "Bostan Dyanamics"      # class variable

    def __init__(self):                # constructor # this def called method
        print("In Construction")
        self.empId = 10                # instance variable
        self.empName = "Vaibahv Rasal"

    def EmpName(self):                 # function 
        print(self.empId)
        print(self.empName)

obj = Employee()                       # object created for Employee() class
obj.EmpName()


