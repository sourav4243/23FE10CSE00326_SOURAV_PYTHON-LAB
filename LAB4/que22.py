# 22. Write a program to display the following pattern:
# 1
# 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0 1 0

n = int(input("Enter num of rows: "))
f = 0
for i in range(n):
    for j in range(2 * i + 1):
        if f == 0:
            print(1, end=" ")
            f = 1
        else:
            print(0, end=" ")
            f = 0
    print()