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
    guessedletter=guessedletter + guess + '_'
    print('current guessed letters are',guessedletter)
    if guess in word:
        print('correct , you still have',lives,'lives left')