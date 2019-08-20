# The first program starts here.
time = input('\nGive a time: ')
clock = float(time)

if clock < 7:
    print('There is still time to sleep.')
elif clock <= 8:
    print('Time to wake up and go to work.')
elif clock <= 10:
    print('You are a little bit late but you can still make it.')
else:
    print('It is better to stay home at this point')
# The first program ends here.

# The second program starts here.
name = input('\nGive you name ')

if name == 'John':
    print('How are you' + ' ' + name)
elif name == 'Sarah':
    print('How are you' + ' ' + name)
else:
    print('You are a new person to me. Nice to meet you' + ' ' + name)
# The second program ends here.

# The third program starts here.
number = input('\nGive a number: ')
userInput = float(number)

if userInput < 10:
    print('You inserted number' + ' ' + number + ' ' + 'and it is smaller than 10')
elif userInput < 100:
    print('You inserted number' + ' ' + number + ' ' + 'and it is smaller than 100')
elif userInput < 1000:
    print('You inserted number' + ' ' + number + ' ' + 'and it is smaller than 1000')
else:
    print('You inserted number' + ' ' + number + ' ' + 'and it is bigger than 1000')
# The third program ends here.

# The fourth program starts here.
print('\nInsert three numbers and the program will tell you which is the biggest one.\n')

firstNumber = int(input('Insert the first number: '))
secondNumber = int(input('Insert the second number: '))
thirdNumber = int(input('Insert the third number: '))

if firstNumber < secondNumber:
    if secondNumber < thirdNumber:
        print('\nThird number is the biggest one.')
    else:
        print('\nSecond number is the biggest one.')
else:
    if firstNumber < thirdNumber:
        print('\nThird number is the biggest one.')
    else:
        print('\nFirst number is the biggest one.')
# The fourth program ends here.
