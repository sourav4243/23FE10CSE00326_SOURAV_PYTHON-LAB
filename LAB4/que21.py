# 21. Write a program to display the following pattern:
# A
# B A B
# A B A B A
# B A B A B A B

n = int(input("Enter num of rows: "))
f = 0
for i in range(n):
    for j in range(2 * i + 1):
        if f == 0:
            print("A", end=" ")
            f = 1
        else:
            print("B", end=" ")
            f = 0
    print()