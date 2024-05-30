##number_hippos = 1
##more_hippos = "yes"
##while more_hippos == "yes":
##    number_hippos += 1
##    print("You have", number_hippos, "hippos!")
##    more_hippos = input("Do you want another hippo?")

##game_completed= True
##while game_completed:
##    print('GL Finish the Game')

##game_completed= False
##while game_completed:
##    print('GL Finish the Game')
##
##secret_word = 'Bottle'
##guess= input('Guess the secret word:')
##while guess!=secret_word:
##    print('Try Again')
##    guess= input('Guess the secret word:')
##print('You got it!')

##secret_word = 'Bottle'
##a="I don't know!"  
##while True:
##    guess= input('Guess the secret word:')
##    if guess == secret_word:
##        print('Correct Word')
##        break
##    elif guess == a:
##        print('The word was Bottle')
##        break
##    else:
##        print('Try Again')
##secret_word = 'Bottle'       
##="I don't know!"   
##guess= input('Guess the secret word:')
##while guess != secret_word and guess !=a:
##    print('Try again!')
##    guess= input('Guess the secret word:')
##print('Correct word is Bottle')
    
##user_num= int(input('Enter a number:'))
##while user_num %2 != 0:
##    print('Try Again')
##    user_num= int(input('Enter a number:'))
##print('Your number is even')

for i in range(2,9):
    print(i)
num=2
while num<=8:
    print(num)
    num=num+1
guess = int(input("Guess the number of marbles in the jar: "))
number_of_marbles = 249
while guess != number_of_marbles:
    print("Incorrect guess! Try again!")
    guess = int(input("Guess the number of marbles in the jar: "))
print('Good job you got it')
