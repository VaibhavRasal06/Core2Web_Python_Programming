# Shallow Copy

lang = ["CPP", "Java", "Python", ["Go", "Rust", "Dart"]]
print(lang)

newList = lang.copy()
print(newList)

print(id(lang) == id(newList)) # False

lang[3][1] = "JavaScript"
print(lang)

print(newList)

