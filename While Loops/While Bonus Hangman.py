word = 'House'
print('Lets play hangman')
user_guess = input('Now guess my word:')
while user_guess != word :
    user_guess= input('Try Again:')
print('You got it!')
