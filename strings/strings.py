firstWord = 'high'
secondWord = 'school'

print(firstWord + secondWord)

word = 'highschool'

print(word[4])  # This will print the letter 's' because arrays starts at the number 0.
print(word[0:4])  # This will print the word high.
print(word[4:10])  # This will print the word school.
print(word[0:5:2])  # This will print the letters 'h' 'g' 's'.
print(word[4:])  # This will also print the word school.
print(word[0::2])  # This will print every other letter.
print(word[::])  # This will print the whole word.
print(word[:4] + word[4:])  # This will print the word highscool.
print('n' + word[1:4] + 't' + word[4:10])  # This will print the word nightschool.
print(word[-1])  # This will print the last letter of the word.
print(word[:-2])  # This will print the word without the last two letters.
print(word[::-1])  # This will print the word backwards.
print(len(word))  # This will print how many letters there are in word.

age = 15
print(str(age) + '-year-old\n')  # This allows to print string and int.

inputWord = input('Give a word: ')
cut = input('Give a number and the program will cut the word at that point. ')
count = int(cut)
print('\nOnce the word' + ' ' + inputWord + ' ' + 'is cut' + ' ' + 'it is' + ' ' + inputWord[0:count])
