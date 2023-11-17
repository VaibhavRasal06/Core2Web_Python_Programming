# Deep Copy

import copy as cp

lang = ["CPP", "Java", "Python", ["Go", "Rust", "Dart"]]

newList = cp.deepcopy(lang)

print(lang)
print(newList)

lang[3][2] = "JavaScript"

print(lang)
print(newList)
