# write a program that accepts strings and calculate the number of uppercase and lowercase letters in the string
def counter(s):
    upper=lower=0
    for i in s:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
    print(f"Number of uppercase letters = {upper}\nNumber of lowercase letters = {lower}")

counter(input("Enter string: "))