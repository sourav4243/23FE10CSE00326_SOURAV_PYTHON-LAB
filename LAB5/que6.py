# 6. write a python program to convert all characters into uppercase and lowercase and eliminate duplicate letters from given sequence using map
seq = input("Enter sequence: ")

uppercase = "".join(list(map(lambda x: x.upper(), seq)))
lowercase = "".join(list(map(lambda x: x.lower(), seq)))

No_duplicates_upper = "".join(dict.fromkeys(uppercase))
No_duplicates_lower = "".join(dict.fromkeys(lowercase))

print("Uppercase:",uppercase)
print("Lowercase:",lowercase)
print("Uppercase without duplicates:",No_duplicates_upper)
print("Lowercase without duplicates:",No_duplicates_lower)