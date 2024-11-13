# write a program to take vairable lengh arguments in function and perform cube of each element
def cube(*args):
    res = [ x**3 for x in args]
    return res

print(cube(1,2,3,4,5,6))