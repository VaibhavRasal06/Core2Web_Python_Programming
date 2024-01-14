"""Write a real-time example of OOP on IPL cricket by the following point.
a. Instance variable
b. constructor
c. Class variable
d. Instance method"""

class IPL:

    total_teams = 8

    def __init__(self,team_name,team_captain):
        self.team_name = team_name
        self.team_captain = team_captain

    def IPL_team_info(self):
        print(self.team_name)
        print(self.team_captain)

team1 = IPL("Mumbai Indians","Rohit Sharma")
team2 = IPL("Chennai Super Kings", "MS Dhoni")

print(IPL.total_teams)

team1.IPL_team_info()
team2.IPL_team_info()
