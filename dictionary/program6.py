# Others

# 1. copy()
# 2. update()
# 3. setdefault()
# 4. fromkeys

player = {45:"Rohit", 77:"Shubhman", 18:"Virat",96:"Shreyash","next to bat":{1:"KLRahul",63:"SKY",8:"Jaddu"}}

print(player)

newData = player.copy()
print(newData)

newData = {33:"hardik",20:"Shami"}
player.update(newData)

print(player)

player.setdefault(19,"Kohli")
print(player)

player1 = {}

lang = ["ReactJS","Fluter","SpringBoot"]
teacher = "Shashi"

print(player1.fromkeys(lang,teacher))
