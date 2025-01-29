word='bus'
blank=''
guessedletter=''
for i in (word):
    blank=blank + '_'
lives=7
print(blank)
while '_' in blank:
    word='bus'
    guess = input('enter a letter:')
    guessedletter=guessedletter + guess + ','
    print('current guessed letters are',guessedletter)
    if guess in word:
        print('correct , you still have',lives,'lives left')
    else:
        guess!=word+'_'
        lives=lives-1
        print('incorrect you have',lives,'lives left')
        
    if lives==0:
        print('you have no lives left, GAME OVER')
        
if '_' not in blank and lives>0:
    print('YOU WIN')
    
else:
    guessedletter=='b','u','s'
    print('YOU WIN')
    
        