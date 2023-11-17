# Delete elemets from dictionary

# 1. pop()
# 2. popitems()
# 3. clear


player = {45:"Rohit", 77:"Shubhman", 18:"Virat",96:"Shreyash","next to bat":{1:"KLRahul",63:"SKY",8:"Jaddu"}}

print(player)

player.pop(77)
print(player) # delete only mentioned key value pair

player.popitem()
print(player) # delete last element

player.clear()
print(player)


