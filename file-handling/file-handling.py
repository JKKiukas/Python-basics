# The first program starts here.
text = '''\
Hello World
This is our new text file
and this is another line.
Why? Because we can.
'''

file = open("textFile.txt", "w", encoding="utf-8")
file.write(text)
file.close()

file = open("textFile.txt", "r", encoding="utf-8")
while True:
    line = file.readline()
    if len(line) == 0:
        break
    print(line, end="")
file.close()
# The first program ends here
