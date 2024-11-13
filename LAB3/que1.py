# 1. wap to find a number is Prime or not.
num = int(input("Enter num:"))
isPrime = True
for i in range(2,num):
    if num%i ==0:
        isPrime = False
        break
if isPrime==True:
    print("Prime")
else:
    print("Not Prime")