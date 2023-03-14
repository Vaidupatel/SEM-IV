#Write a program that creates a function for nth Fibonacci number

def fib(n):
    if (n==1):
        return 0
    elif(n==2):
        return 1
    else:
        a=0
        b=1
        for i in range(n-2):
            c=a+b
            a=b
            b=c
        return c 
    
n=int(input("Enter the position to know fibonacci number"))
print("The fibonacii number at ",n,"is ",fib(n))
