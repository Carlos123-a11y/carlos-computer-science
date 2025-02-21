#page 223 electronic copy questions
#question 1
'''
a=input('enter a list:')
list_of_input=list(a)
list_of_input.reverse()
print(list_of_input)



#question2
lst1=[input('enter a word:')]  
lst2=[input('enter a word too add it to the first list:')]
lst3=lst1+lst2
print(lst3)
#3

list2=input('enter a list of 1-12:')
lista=list(list2)
lenght=len(list2)
for i in range(0,lenght):
    if i >10:
        lista[i]=10
        
print(lista)

#4
strings=input('enter a string:').split()
modified_string=[s[1:] for s in strings if len(s)>0]
print('modified_string:',modified_string)

#5 #a
list_a=[i for i in range(50)]
print(list_a)

#b
list_b=[i**2 for i in range(1,51)]
print(list_b)
#c
list_c=[chr(97+i) * (i+1) for i in range(26)]
print(list_c)
'''
#6
L=[3,1,4]
M=[1,5,9]
N=[L[0:1+1]+M[0:1+1]]
print(N)



#7
lst=[1,2,3,4,5,6,7,8]
lst.reverse()
print(lst)
#8

