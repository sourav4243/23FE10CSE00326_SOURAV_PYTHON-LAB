# 3. wap to find the grade of student using given percentage
percentage = int(input("Enter precentage:"))
if percentage >90:
    print("A")
elif 80<percentage<=90:
    print("B")
elif 70<percentage<=80:
    print("C")
elif 60<percentage<=70:
    print("D")
else:
    print("F")