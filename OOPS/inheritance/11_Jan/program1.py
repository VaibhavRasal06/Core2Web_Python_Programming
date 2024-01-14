
class Boss:

    def report(self):
        print("Mich ahe Boss")

class Manager(Boss):
    
    def report(self):
        print("Manager: Report to Boss")

class TeamLead(Manager,Boss):

    def reprot(self):
        print("TeamLead: Report to Manager and Boss")

class Developer(TeamLead):

    def report(self):
        print("Developer: Report to TeamLead")

print(Developer.mro())
