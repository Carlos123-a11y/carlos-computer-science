#2
if temp<32:
    print('ice')
elif temp<212:
    print('water')
else:
    print('steam')
    
#3
    
x=1
if x >3:
    print('A',end='')
else:
    print('B',end='')
elif x<2:
    if(x!=0):
        print('C',end='')
        
#4
weather='raining'
if weather='sunny':
    print('wear sunblock')
elif weather='snow':
    print('going skiing')
else:
    print(weather)
    
#5
if int('zero')==0:
    print('zero')
elif str(0)=='zero':
    print(0)
elif str (0)=='0':
    print(str(0))
else:
    print('none of the above')
    
    
#6
if n ==0:
    print('zero')
elif:n==1:
    print('one')
elif n==2:
    print('two')
else n==3:
    print('three')
    
#7
n=int(input('enter a number'))
if n<1:
    print('invalid value')
else:
    for i in range(1,n+1):
        print(i*i)
        
        
#8









#9
i=100
while(i>0):
    print(i)
while num>0:
    print(num%10)
    num=unm/10
while num>0:
    count+=1
    sum+=num
        sum+=num
        num-=2
        if count==10:
            print(sum/float(count))
            break
        
#10
mins=0
maxs=mins
while num <0:
    mins=num
    maxs=0
    for i in range(mins,maxs+1):
        sums+=1
        
#11
#a
count=0
while count<10:
    print('helllo')
    count+=1
    
#b
x=10
y=0
while x>y:
    print(x,y)
    x=x-1
    y=y+1
    
#c
keepgoing=true
x=100
while keepgoing:
    print(x)
    x=x-10
    if x <50:
        keepgoing=false
        
#d
x=45
while x<50:
    print(x)
#e
for x in [12345]:
    print(x)
    
#f
for x in range(5):
    print(x)
    
#g
for p in range(1,10):
    print(p)
    
#h
for q in range(100,50,-10):
    print(q)
    
#i
for z in range(-500,500,100):
    print(z)
#j
for y in range(100,50,-10):
    print('*',y)
    
#k
x=10
y=5
for i in range(x-y*2):
    print('%',i)
    
#l
for x in [123]:
    for y in [4,5,6]:
        print(x,y)
        
#m
for x in range(3):
    for y in range(4):
        print(x,y,x+y)
        
#n
for x in range(10):
    for y in range(5):
        c+=1
    print(c)
    
#12
for i in range(4):
    for j in range(5):
        if i+1==j or j+1==4:
            print('+',end ='')
        else:
            print('o',end ='')