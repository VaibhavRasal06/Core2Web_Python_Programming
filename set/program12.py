# frozenset()

setData = frozenset([1,2,3,4,5])
print(setData)

setData.add(7)
print(setData) # AttributeError: 'frozenset' object has no attribute 'add'
