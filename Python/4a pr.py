# Find out the list of subjects of a particular semester from the input provided as a list of dictionaries using lambda map and filter together.
# i/p:- [{'sem':6,'sub':'python'}, {'sem':6,'sub':'cns'}, {'sem':5,'sub':'java'}, {'sem':5,'sub':'daa'}]
# o/p:-    sem 6
# subjects: ['python','cns']
  
a={0:{}, 1:{}, 2:{}, 3:{} }
b=[]
for i in range(len(a)):
    a[i]['sem']=int(input('Enter sem: '))
    a[i]['sub']=(input('Enter sub: '))
    b.append(a[i])
print(b)    
sem=int(input('Enter sem you want: '))
print(list(map(lambda x:x['sub'], filter(lambda x:x['sem']==sem,b))))

