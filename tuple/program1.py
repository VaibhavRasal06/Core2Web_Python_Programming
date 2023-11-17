# tuple in python

lang =("CPP", "Java", "Python",("Go", "Rust", "Dart"))

print(lang)
print(type(lang))

lang[3][1] = "JavaScript"
print(lang)                  # TypeError
