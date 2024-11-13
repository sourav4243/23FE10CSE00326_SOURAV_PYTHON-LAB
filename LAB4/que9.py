# 9. WAP to check whether the given number is perfect or not
# perfect number is a number which is equal to sum of its positive proper divisors except number itself
num = int(input("Enter num: "))
sum=0
for i in range(1, num//2+1):
  if num % i == 0:
    sum+=i
if num == sum:
  print(num,"is a perfect number")
else:
  print(num,"is not a perfect number")