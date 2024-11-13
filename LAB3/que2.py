# 2. wap to find the given numner is palinndrome or not.
num = input("Enter num:")
if num == num[::-1]:
    print(int(num),"is Palindrome.")
else:
    print(int(num),"is not Palindrome.")
    