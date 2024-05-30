##A function helps accomplish a task for where, suppose you want to find the minimum of 3 numbers. Functions can help you do that with ease.
##If you give an integer for the len function it expects for a string
str_1=input('Enter your first name:')
str_2=input('Enter your middle name:')
str_3=input('Enter your last name:')
print('The length of your full name is:',len(str_1)+len(str_2)+len(str_3))

##a = [1,2,3,4]
##b = [5,6,7,8]
##c = [9,10]
##sum_of_a = sum(a)
##sum_of_b = sum(b)
##sum_of_c = sum(c)
##sum_of_all=sum_of_a+sum_of_b+sum_of_c
##print("The sum of your 3 numbers is", sum_of_all)

first_mark = int(input('Enter your mark from a class:'))
second_mark = int(input('Enter your mark from different class:'))
third_mark = int(input('Enter your mark from different class:'))
highest_mark= max(first_mark,second_mark,third_mark)
print(highest_mark)
