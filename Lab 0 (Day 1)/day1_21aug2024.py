msg = "hello python"
print(msg)
hello python


name= "sourav kumar"
print(name)
sourav kumar


first_name = "sourav"
last_name = "kumar"
full_name = first_name + last_name
print(full_name)
souravkumar


print(first_name,last_name,sep=" ")
sourav kumar

full_name = f"{first_name}{last_name}"
print(full_name)
souravkumar


print(name.title())
Sourav Kumar


print("hello",name)
hello sourav kumar

print("hello",name.title())
hello Sourav Kumar
hello Sourav Kumar
SyntaxError: invalid syntax
naam = input("enter your name")
enter your namesourav
print(naam)
sourav
print(input("enter your name: "))
enter your name: sourav kumar
sourav kumar
>>> firstName = input('enter first name"
...                   
SyntaxError: unterminated string literal (detected at line 1)
>>> firstName = input('enter first name')
...                   
enter first namesourav
>>> lastName = input('enter last name')
...                   
enter last namekumar
>>> print(f"{firstName}{lastName}")
...                   
souravkumar
>>> a=input(enter any number
...         
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a=input("enter any number")
...         
enter any number38
>>> print(a)
...         
38
>>> b=input("enter another number")
...         
enter another number2
>>> print(a+b)
...         
382
>>> print(type(a+b))
...         
<class 'str'>
>>> a=int(input("enter nuber a :"))
...         
enter nuber a :5
>>> b=int(input("enter nuber b :"))
...         
enter nuber b :10
>>> c=a+b
...         
>>> print(c)
...         
15
>>> a= float(input("enter a"))
...         
enter a5.66
>>> b=float(input("enter b"))
...         
enter b3.51
>>> print(a+b)
...         
9.17