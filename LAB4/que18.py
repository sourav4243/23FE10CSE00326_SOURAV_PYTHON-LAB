# 18. Write a program to display the following pattern:
#  * * * * * * * * *
#    * * * * * * *
#      * * * * *
#        * * *
#          *
n = int(input("Enter number of rows: "))
for i in range(n):
    print("  " * i, end="")
    print("* " * (2 * (n - i) - 1))