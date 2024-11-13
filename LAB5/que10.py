# 10. wap to compute the square of first n fibonacci numbers using map and generate a list of numbers
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter the value of n: "))
fibonacci_numbers = list(map(fibonacci, range(n)))
square_fibonacci = list(map(lambda x: x**2, fibonacci_numbers))
print(square_fibonacci)