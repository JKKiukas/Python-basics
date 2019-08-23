# The first program starts here.
def say_hello(name, studying, year):
    print("\nHello " + name)
    print("So you are studying " + studying)
    print("And you have been studying for " + year + " years\n")


say_hello('Jack', 'Software engineering', '2')


# The first program ends here.

# The first program starts here.
def user_info():
    print("\nHello " + name)
    print("So you are studying " + studying)
    print("And you have been studying for " + year + " years\n")


name = input('Give your name: ')
studying = input('what are you studying?: ')
year = input('How many years have you been studying?: ')

user_info()


# The first program ends here.

# The second program starts here.
def maximum(x, y):
    if x > y:
        bigger = x
    else:
        bigger = y
    return bigger


print('Program asks you to give two numbers and it will tell you which one is bigger. '
      'Do not give two same numbers.\n')

firstNumber = int(input('Give first number: '))
secondNumber = int(input('Give second number: '))
bigger = maximum(firstNumber, secondNumber)
print("You gave numbers", firstNumber, "and", secondNumber, "and number", bigger, "is bigger.\n")

# The second program ends here.

# The third program starts here.
print('\nProgram asks you to give a string and a number. The string will be printed the amount of the given number.')


def function(text, repeater):
    for i in range(0, repeater):
        print(text)


string = input('Give a string: ')
number = int(input('Give a number: '))

function(string, number)
function('Table', 3)  # This will print word 'Table' three times.
# The third program ends here.
