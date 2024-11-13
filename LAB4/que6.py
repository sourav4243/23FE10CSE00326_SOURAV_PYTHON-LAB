# 6. WAP to generate the fibonacci series
n = int(input("Enter number of terms: "))
if n==1:
  print(0)
else:
  n1,n2 = 0,1
  print(n1,n2,end=' ')
  for _ in range(2,n):
    n3 = n1+n2
    print(n3,end=' ')
    n1,n2 = n2,n3