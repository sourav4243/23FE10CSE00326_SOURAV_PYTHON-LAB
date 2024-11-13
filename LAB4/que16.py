# 16. Write a program to display the following pattern:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    print("* " * (2 * i - 1))