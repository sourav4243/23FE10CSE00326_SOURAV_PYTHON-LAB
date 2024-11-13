# 9. wap to create a new list taking specific elements from a tuple and convert a string value to an integer
tuple=(10, 'apple', '25', 3.14, 'banana')
newlist=[]
newlist.append(tuple[0])
newlist.append(int(tuple[2]))
print(newlist)