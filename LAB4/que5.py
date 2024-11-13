# 5. WAP to compute the value of nCr
import math
n = int(input("Enter n: "))
r = int(input("Enter r: "))

print(f"nCr = {math.factorial(n) / (math.factorial(r) * math.factorial(n - r))}")