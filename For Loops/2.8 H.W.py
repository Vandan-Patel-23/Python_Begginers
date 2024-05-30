symbol=0
for i in range(1,7):
    print('*'*i)

symbol=0
for i in range(6,0,-1):
    print('*'*i)

fav_letter = str(input('Enter your favourite letter:'))
fav_word = str(input('Enter your favourite word'))
count=0
for i in fav_word:
    if i == fav_letter:
        count=count+1
print(count)

space_count=0
sentence = str(input('Enter a sentence:'))
for i in sentence:
    if i==' ':
        space_count=space_count+1
print('Your sentance has',space_count+1,'words.')

for i in range(0,100,5):
    print(i)

##an iterator variable is like a variable but every iteration the value changes the iterato

##a range is used in a for loop and it takes upto 3 pieces of input. 1 peice of input will be an end point. 2 peices of input will be a start and end. 3 peices of input will be a start, end, and skip.
