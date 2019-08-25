# The first program starts here
try:
    number = int(input("\nGive a number: "))
    print("You gave number", number)
except ValueError:
    print("You tried to give a string. Give a number.")
else:
    print("No error was found.")
# The first program ends here.

