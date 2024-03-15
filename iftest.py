users=['admin','a','b','c','d']
if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like see a status report? ')
        else:
            print(f'Heelo {user.title()}, thank you for logging in again. ')
else:
    print('We need to find some users.\n')
print('\n')


current_users=['1','2','3','4','5']
new_users=['a','b','1','2','c']
for user in new_users:
    if user in current_users:
        print('This user is used. ')
    else:
        print('You can user this name. ')
print('\n')


numbers=range(1,10)
number_list=[]
for number in numbers:
    if number == 1:
        number_list.append(f'{number}st')
    elif number == 2:
        number_list.append(f'{number}nd')
    elif number == 3:
        number_list.append(f'{number}rd')
    else:
        number_list.append(f'{number}th')
for number in number_list:
    print(number)
print('\n')