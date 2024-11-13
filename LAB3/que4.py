# 4. wap to create a simple console base calculator
a = int(input("Enter num 1:"))
b = int(input("Enter num 2:"))
operator = input("Enter operator: +, -, *, /, **, //")
if operator =="+":
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    print(a/b)
elif operator == '**':
    print(a**b)
elif operator == '//':
    print(a//b)