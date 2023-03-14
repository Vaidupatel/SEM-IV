# Write a python program to check whether the given string is a palindrome or not.

a=input("enter the strint to know that is palindrome or not\n")
b=''
for i in a:
    b=i+b
if(a==b):
    print(a," is palindrome")
else:
    print(a," is not palindrome")
