##user_word = input('Enter a word')
##hangman_yes_no = input('Do you wanna play hangman:')
##if hangman_yes_no == 'Yes' or hangman_yes_no == 'yes':
##    print('Ok lets play')
##else:
##    print(':(')
##for l in user_word:
##    print('_',end=' ')
##for i in range(5):
##    letter = input('Enter a letter:')
##    for l in user_word:
##        if letter == l:
##            print(letter,end=' ')
##        else:
##            print('_',end=' ')

##import random
##num=random.randrange(0,10)
##print(num)
##user_guess= int(input('Enter a number:'))
##while user_guess!= num and user_guess<10:
##    if user_guess>num:
##        print('Your guess is too high')
##    else:
##        print('Your guess is too low')
##
##    print('Try again')
##    user_guess= int(input('Enter a number:'))
##    
##print('the number',num)


##user_num= int(input('Enter a number:'))
##s=int(input('Starting postition:'))
##e=int(input('Ending position:'))
##for i in range(s,e+1):
##    print(user_num,'*',i,'=',user_num*i)

num=int(input('Enter a number you want to factorize:'))
for i in range(1,num+1):
    if num % i ==0:
        print(i,end=', ')
