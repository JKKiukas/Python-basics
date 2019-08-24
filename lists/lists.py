# The first program starts here.
shoppingList = ['soap', 'toothpaste', 'cheese', 'bread']
print("I need", len(shoppingList), "products")
print("These products are:", end=" ")
for product in shoppingList:
    print(product, end=" ")

print("I need to buy a brush also.")
shoppingList.append("brush")  # append adds one item to the list
print("Now my shopping list looks like this:", shoppingList)
print("Lets reorganize the shopping list.")
shoppingList.sort()  # sort puts list in alphabetic order
print("Reorganized shopping list looks like this:", shoppingList)

print("The first product I need to buy is", shoppingList[0])
bought = shoppingList[0]
del shoppingList[0]  # del removes one item from the list. In this case it removes the first item from the list.
print("I just bought", bought)
print("Now there are just", shoppingList, "left on my shopping list.")


# The first program ends here.

# The second program starts here.
class Student:
    firstName = ""
    lastName = ""
    studentID = "0"


students = []

firstStudent = Student()
firstStudent.firstName = "John"
firstStudent.lastName = "Doe"
firstStudent.studentID = "123456"

secondStudent = Student()
secondStudent.firstName = "Sarah"
secondStudent.lastName = "Doe"
secondStudent.studentID = "654321"

students.append(firstStudent)
students.append(secondStudent)

for Student in students:
    print("\nName:", Student.firstName)
    print("Last name:", Student.lastName)
    print("Student ID:", Student.studentID)
# The second program ends here.

# The third program starts here.
thisIsList = []

while True:
    number = int(input("\nGive two positive number (negative number stops the program): "))
    if number < 0:
        break
    thisIsList.append(number)

print("\nThese numbers are in the list:", thisIsList)
thisIsList.sort()
print("When the list is sorted it looks like this:", thisIsList)
thisIsList.pop(0)
thisIsList.pop()
print("The list looks like this when the first and the last number is removed:", thisIsList)
# The third program ends here.
