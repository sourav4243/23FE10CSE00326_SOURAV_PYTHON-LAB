# 19. Write a program to display the following pattern (Pascal Triangle):
#         1
#       1   1
#     1   2   1
#   1   3   3    1
#  1  4   6   4   1
# 1  5  10  10  5   1
from math import factorial
n = int(input("Enter number of rows: "))
for i in range(n):
    print(' ' * (n - i), end='')
    num = 1
    for j in range(i + 1):
      num = factorial(i) // (factorial(j) * factorial(i - j))
      print(f"{num}",end=" ")
    print()