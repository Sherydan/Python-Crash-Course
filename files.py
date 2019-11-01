myFile = open('myFile.txt', 'w')

# get some info
print('name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# write to file
myFile.write('I love python')
myFile.write(' and javascript')
myFile.close()

# append to file
myFile = open('myFile.txt', 'a')
myFile.write(' i also like CSGO :^)')
myFile.close()

# READ

myFile = open('myFile.txt', 'r+')
text = myFile.read()
print(text)





