# Using concept of list comprehension, Write a program to transpose m x n matrix.

a= [[1,2],[3,4],[5,6]]
for i in a:
    print(i)
b=[[a[i][j] for i in range(len(a))]for j in range(len(a[0]))]
for i in b:
    print(i)

