# 7. WAP to count the sum of digits in the entered number.
num = input("Enter num: ")
sum = 0
for i in num:
  sum += int(i)
print(sum)