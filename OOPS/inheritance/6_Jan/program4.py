

class Manager:

    def project(self):
        print("In project:Manager")

class TeamLead1(Manager):
    pass

class TeamLead2(Manager):
    
    def project(self):
        print("In Project:TeamLead2")

class Developer(TeamLead1,TeamLead2):
    pass

obj = Developer()
obj.project()
