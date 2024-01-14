
class Boss:

    def report(self):
        print("I'm the Boss")

class Manager1(Boss):

    def report(self):
        print("Manager1: Report to Boss")

class Manager2(Boss):

    def report(self):
        print("Manager2: Report to Boss")

class TeamLead1(Manager2,Manager1):

    def report(self):
        print("TeamLead1: Report to Manager2 and Manager1")

class TeamLead2(Manager2, Manager1):

    def report(self):
        print("Manager2: Report to Manger2 and Manager1")

class Developer(TeamLead2,TeamLead1):
    pass

print(Developer.mro())

