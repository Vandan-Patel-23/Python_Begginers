#STUDENT VERSION

# Here are all your hangman drawings
hangman0 = '''
  +---+
  |   |
      |
      |
      |
      |
========='''

hangman1 = '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
hangman2 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
hangman3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
hangman4 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''
hangman5 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
hangman6 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''

# S1 - ask for user's name and word to guess
player1_name=input('Player 1 enter your name:')
player2_name=input('Player 2 enter your name:')
full_answer=input('Player 1 enter a word or phrase:')
# S2 - initialize important variables
wrong_letters=''
correct_letters=''
lives=6
while lives>=0: # S7
    # S3
    for char in full_answer:
        if char in correct_letters:
            print(char , end=' ')
        else:
            print('_',end=' ')
    print()
    # S4
    if lives==6:
        print(hangman0)
    elif lives==5:
        print(hangman1)
    elif lives==4:
        print(hangman2)
    elif lives==3:
        print(hangman3)
    elif lives==2:
        print(hangman4)
    elif lives==1:
        print(hangman5)
    else:
        print(hangman6)
    # S5
    guessed_letter=input('Player 2 guess a letter: ')
    #S6
    if guessed_letter in wrong_letters  or guessed_letter in correct_letters :
        print('Letter has already been guessed:')
    elif guessed_letter in full_answer:
        if guessed_letter==full_answer:
            print('You guessed the whole word')
            correct_letters+=guessed_letter
            break
        print('You guessed a correct letter')
        correct_letters+=guessed_letter   
    else:
        print('Try Again')
        wrong_letters+=guessed_letter
        lives-=1
# S9, S10 and S11
if lives==-1:
    print('You Won',player1_name)
else:
    print('You Won',player2_name)
    
