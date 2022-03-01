f = open("demofile2.txt", "w")
userInput = input("what is your name")
f.write(userInput)
f.close()

f = open("demofile2.txt")
print(f.read())

