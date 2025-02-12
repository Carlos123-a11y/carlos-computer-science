lst=[10,12,14,20,22,24,30,32,34]
seq=lst[3:-3]
seq
[20,22,24]
seq[1]=28
seq
[20,28,24]
#1
lst=[10,12,14,20,22,24,30,32,34]
print(lst[3:30])
print(lst[-15:7])
#2
L1=[2,3,4,5,6,7,8]
print(L1[2:5])
print(L1[6:10])
print(L1[10:20])
#3
print(lst[0:10:2])
print(lst[2:10:3])
#1
list1=[5,6,8,11,3]
print(list1[::-1])
#2
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
slc1=lst[5:15:2]
slc2=lst[::4]
sum=avg=0
print('slice1')
 
for a in slc1:
    sum+=a
    print(a,end='')
print()
print('sum of elements in slice1:',sum)
print('slice2')
sum=0
for b in slc2:
    sum+=b
    print(b,end='')
print()
avg=sum/len(slc2)
print('average of elements of slice2:',avg)
 
 
L=['one','two','THREE']
L[0:2]=[0,1]
L
print(L)
L=['one','two','THREE']
L[0:2]='a'
L
print(L)
 
L1=[1,2,3]
L1[2:]='604'
L1
lst1=[10,12,14]
lst1.append(16)
lst1
print(lst1)
 
 
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lst.pop()
print(lst)
lst.pop(10)
print(lst)
 
 
a=[1,2,3]
b=a
print(b)
 
a=[1,2,3]
b=a
a[1]=5
a
print(a)
 
a=[1,2,3]
b=list(a)
a[1]=5
a
print(b)
lst=[1,2,3,4,5]
lst1=[6,7,8,9]
lst.extend(lst1)
print(lst)
#nested list 
colours=['red','green','blue']
colours.append('yellow')
print(colours)
lst=[1,2,3]
lst2=lst.append(12)
print(lst2)
print(lst)
t1=['a','b','c']
t2=['d','e']
t1.extend(t2)
print(t1)
t1=['a','e','u']
t1.insert(2,'i')
t1.insert(-9,'k')
print(t1)
ele1=t1.pop(0)
print(ele1)


#t1.remove
t1=['a','e','i','p','q','a','q','p']
t1.remove('a')
print(t1)


#list.clear()
L1=[2,3,4,5]
L1.clear()
print(L1)


L1=[13,18,20,10,18,23]
L1.count(18)
print(L1)


#list.reverse(reverses everything)
t1=['a','b','c','d','e','f']
t1.reverse()
print(t1)


t1=['b','c','a','e']
t1.sort()
print(t1)