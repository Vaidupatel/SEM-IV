# Using concept of list comprehension, Write a program to print the Fibonacci sequence form with a given n input by console.

def fibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
n=int(input("enter the number"))
a=[ fibo(i) for i in range(n)]
print(a)


