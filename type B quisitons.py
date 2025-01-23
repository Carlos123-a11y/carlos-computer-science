#Q1
#(A)
print('''
 1
  2
   3
''')

#(B)
text='Test./nNext line.'
print(text)

#(C)
print('one','two'*2)
print('one'+'two'*2)
print(len('0123456789'))

#(D)
s='0123456789'
print(s[:3],','',',s[0:3],'-',s[2:5])
print(s[:3],'-',s[3],',',s[3:100])
print(s[-100:-3],s[-100:3])


#(E)
s='987654321'
print(s[-1],s[-3])
print(s[-3],s[-1])
print(s[-100:-3],s[-100:3])

#Q2
#(A)
y=str(123)
x='hello'*3
print(x,y)

#(B)
x='hello'+\
'to python'+\
'world'
for char in x:
    y=char
    print(y,':',end='')
    

#(C)
x='hello world'
print(x[:2],x[-2:],x[-2:])
print(x[6],x[2:4])
print(x[2:-3],x[-4:-2])





#Q3
theStr='this is a test'
inputstr=input('enter integer:')
inputint=int(inputstr)
testStr=theStr
while inputint>=0:
    testStr=testStr[1:-1]
    inputint=inputint -1
testbool='t'in testStr
print(theStr)
print(testStr)
print(inputint)
print(testbool)
#4
teststr+'abcdefghi'
inputstr=input('enter a intger')
inputint=int(inputstr)
count=2
newstr=''
while count <=inputint:
    newstr=newstr+teststr[0 :count]
    teststr=teststr[2:0]
    count=count+1
print(newstr)
print(teststr)
print(count)
print(inputint)




























