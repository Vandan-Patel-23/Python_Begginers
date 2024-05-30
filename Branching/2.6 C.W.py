##num1 = float(input("Enter a decimal number: "))
##num2 = float(input("Enter a decimal number: "))
##print("If I print True, both your numbers round to 4!")
##print(round(num1))

##num=int(input('Enter any number'))
##if num == 0:
##    print(num,'is 0')
##elif num > 0:
##    print(num,'is positive')
##else:
##    print(num,'is negative')
##user_birth_year= int(input('enter the year you were born:'))
##if user_birth_year > 2000: # our first branch (pink)
##    print("I am older than you!")
##elif user_birth_year == 2000: # our second branch (blue)
##    print("We are the same age!")
##else:
##    print("You are older than me!") # the last branch (yellow)
##your_favourite_word=str(input('What is your favourite word'))
##my_favourite_word='hi'
##if len(my_favourite_word) > len(your_favourite_word):
##    print("My word is longer!")
##elif len(my_favourite_word) < len(your_favourite_word):
##    print("Your word is longer!")
##else:
##    print("Our words have the same length!")
##    print("They have", \
##len(my_favourite_word),"letters")

##user_age=int(input('Enter your age'))
##if user_age <12 and user_age >=0:
##    print('You are very young')
##elif user_age < 20 and user_age>=12:
##    print('You are a teenager')
##elif user_age > 20 and user_age<=99:
##    print('You are an adult')
##elif user_age>99:
##    print('You are very old')
##else:
##    print('Invalid')

user_num=int(input('Guess the number:'))
if user_num>69:
    print('Your guess it too high')
    user_num=int(input('Try Again!:'))
elif user_num<69:
    print('Your guess it too low')
    user_num=int(input('Try Again!:'))
else:
    print('YOU GOT IT!')
