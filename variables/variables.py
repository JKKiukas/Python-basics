X = 1
Y = 2
Z = 3
print(X + Y)

# Here numbers are strings because of the '' characters.
X = '1'
Y = '2'
print(X + Y)

print(Z + 3)

text = 'This will be printed'
print(text)

number = 4
mathTask = number * 3 + 5
print(mathTask)


length = 10
width = 20
area = length * width
print(area)
print('ring is ', 2 * (length + width))

# Here we will get the users input
i = input("Give a circle's ring ")
ring = int(i)
pi = 3.14

area1 = ring * ring * pi
print('Area is', area1)
print('Ring is', 2 * ring * pi)

word = input('Give a word or words: ')
print('You gave a word or words', word)
