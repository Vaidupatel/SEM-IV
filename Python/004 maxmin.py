a={'vaidik':508,'sahil':515,'prince':510,'darshan':491,'nirjal':332}
b=max(a,key=a.get)
c=min(a,key=a.get)
    
print("Maximum key is",b," and value is ",a[b])
print("Minimum key is ",c," and value is ",a[c])
