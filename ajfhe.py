row1=['1','2','3']
row2=['4','5','6']
row3=['7','8','9']
row1[0=='']
print( row1,'\n',row2,'\n',row3)
player1=input(' player1 enter a number')
player2=input(' player2 enter a number')

if player1=='1':
    row1[0]='x'
    print(row1,'\n',row2,'\n',row3)
    
    
if player2=='2':
    row1[1]='o'
    print(row1,'\n',row2,'\n',row3)
    
if player1=='3':
    row1[2]='x'
    print(row1,'\n',row2,'\n',row3)

