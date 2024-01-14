
class Boss:

    def reprot(self):
        print("I'm the Boss")

class Manager1(Boss):

    def report(self):
        print("Manager1: Report to Boss")

class Manager2(Boss):

    def report(self):
        print("Manager2: Report to Boss")

class TeamLead1(Manager1,Manager2):

    def report(self):
        print("TeamLead1: Report to Manager1 and Manager2")

class TeamLead2(Manager2):

    def report(self):
        print("teamLead2: Report to Manager2")

class Developer(TeamLead1,TeamLead2):
    pass

print(Developer.mro())
