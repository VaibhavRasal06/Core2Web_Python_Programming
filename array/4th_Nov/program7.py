# 4. extend()

import array as arr

building_no = arr.array('u',['A','B','C','D'])

print("Without extend(): ",building_no)

building_no.extend('E')

print("with extend(): ",building_no)
