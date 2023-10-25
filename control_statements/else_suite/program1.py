studentList = ["Vaibhav", "Vikee", "Aashish", "Yash", "Lambodar"]
studentName = input("Enter here student name: ")

for student in studentList:
    if student == studentList:
        print(studentName, "prsent in list")
else:
    print(studentName,"Not present in list")
