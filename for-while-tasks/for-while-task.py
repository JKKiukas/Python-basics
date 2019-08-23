# The first program starts here.
right_number = 50

print('\nThe program will ask the user to give a number and if it is correct the program stops\n')

while True:
    guess = int(input('Guess the right number: '))
    if guess == right_number:
        print('\nCongratulation you got the right number.')
        print('Thank you for participating.')
        break
    elif guess < right_number:
        print('\nThe number you guessed was too small.')
    else:
        print('\nThe number you guessed was too big.')
# The first program ends here

# The second program starts here.
print('\nThe program will print numbers from 1 to 10.')

for i in range(1, 11):
    print(i)
# The second program ends here

# The third program starts here.
print('\nThe program will find the lucky number and after that it stops.\n')

for i in range(1, 11):
    if i == 7:
        print("The lucky number", i, "was found.")
        break
    print("Lets search the number", i)
# The third program ends here

# The fourth program starts here.
# Learning how the continue statement works.
print('\nWrite stop whenever you want to stop the program.')

while True:
    string = input('Give a string: ')
    if string == 'stop':
        print('Program was stopped.')
        break
    if len(string) < 5:
        continue
    print('String was over 4 characters')
# The fourth program ends here

# The fifth program starts here.
while True:
    repeater = int(input('\nGive a number and the word will be repeated that many times (0 = stop): '))
    if repeater == 0:
        print('Program was stopped.')
        break
    word = input('Give a word that will be repeated: ')
    print('')
    for i in range(0, repeater):
        print(word)
# The fifth program ends here
