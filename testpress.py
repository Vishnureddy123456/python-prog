#1
a=input('enter a string: ')
print(a[::-1])
#2
a=int(input('enter the number: '))
if a>1:
    for i in range(2,a//2+1):
        if a%i==0:
            print('No')
            break
    else:
        print('Yes')
else:
    print('No')

#3
a=eval(input('enter the input: '))
c=a[::-1]
b=''
for i in c:
    b+=str(i)
print(b)
#4
a=int(input('enter a number: '))
res=0
i=len(str(a))-1
while a>0:
    r=a%10
    res+=(r*10**i)
    a//=10
    i-=1
print(res)
#5
a=eval(input('enter the list: '))
print(max(a),min(a))
