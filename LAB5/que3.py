# 3. write a python program to listify the list of given strings individually using python map
l = ["hello", "world", "python"]
print(list(map(lambda x: list(x), l)))