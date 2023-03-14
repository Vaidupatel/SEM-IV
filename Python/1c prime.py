# Write a function to find all prime numbers occur between 100 to 200

def f1(x):
     Flag=False
     for i in range(2,x):
          if x%i==0:
               Flag=True
               break
     if Flag:
          print('The',x,'is prime')
     else:
          print('The',x,'is not prime')
for j in range(100,201):
     x=j
     f1(x)



