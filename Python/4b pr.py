# Write a program to count frequency of elements and storing in dictionary using zip().


a=input('Enter string')
b=a.split(' ')
c=[]
print(b)
for i in b:
    c.append(b.count(i))
print (c)
d=dict(zip(b,c))
print(d) 

