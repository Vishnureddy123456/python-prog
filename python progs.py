#padding the even and odd elements to the strings 
l=eval(input('enter the input: '))
s=input('enter the string: ')
e=[]
summ=0
a=1
output=''
for i in range(len(l)):
    summ+=l[i]
    if a==1:
        if summ%2==0:
            e.append(summ)
            summ=0
            a=0
    if a==0:
        if summ%2==1:
            e.append(summ)
            summ=0
            a=1
if len(s)>len(e):
    c=e[:len(e):][::-1]
else:
    c=e[:len(s):][::-1]
print(c)
for i in range(-1,-len(s)-1 if len(e)>len(s) else -len(e)-1,-1):
    output+=str(c[i])+s[i]
print('output is:', output)

#padding the string in same order as it reverse
#i am college student-input
#t ne dutsege llocmai-output

s=input('enter a string: ')
c=''
a=s.split()
b=(''.join(a))[::-1]
k=0
for i in range(len(a)):
    t=0
    for j in range(len(b)):
        l=len(a[i])
        c+=b[k]
        t+=1
        k+=1
        if t==l:
            break
    c+=' '
print(c)
#enter the no of rows: 5
#1 2 3 4 5 
#  5 4 3 2 
#    2 3 4
#      4 3 
#        3
#pattern
n=int(input('enter the no of rows: '))
sp=0
st=n
dummy=1
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for j in range(st):
        print(dummy,end=' ')
        if i%2==0:
            if j<st-1:
                dummy+=1
            else:
                pass
        else:
            if j<st-1:
                dummy-=1
            else:
                pass
    
    st-=1
    sp+=1
    
    print()
