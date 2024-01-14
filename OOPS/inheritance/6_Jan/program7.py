

class Director:

    def college(self):
        print("Derector of college")

class Principal(Director):

    def college(self):
        print("Principal of college")

class HOD(Principal):

    def college(self):
        print("HOD of Department")

class Teacher1(HOD):

    def college(self):
        print("Teacher1 of Department")

class Teacher2(HOD):

    def college(self):
        print("Teacher2 of Deparment")

class Teacher3(HOD):

    def college(self):
        print("Teacher3 of Department")

class Student(Teacher1,Teacher2, Teacher3):

    def college(self):
        print("Student of college")


print(Student.mro())
