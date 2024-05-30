# 1
for i in range(4):
   for j in range(4):
       print('*',end=' ')
   print()

# 2
user_star= input('Do you want to have more stars:')
while user_star == 'yes':
   for i in range(4):
       for j in range(4):
           print('*',end=' ')
       print()
   user_star= input('Do you want to have more stars:')

# 3
user_name = input('Enter your name:')
for i in range(3):
   for j in range(5):
       print(user_name,end=' ')
   print()

# 4
for i in range(1,11):
   for j in range(1,11):
       print(i*j, end = '\t')
   print()

#5
for i in range(3):
   for j in range(2):
       print('\t|', end=' ')
   if i<=1:
       print('\n','_ '*15,'\n')
print()

#6
for i in range(3):
   print('\n','_ '*16,'\n')
   for j in range(4):
       print('|', end='\t')
print('\n','_ '*16,'\n')
print()
