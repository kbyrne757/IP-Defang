#python version 3.9.5
#IP Address Defang

userInput = input("Enter IP address to be defanged: ")

defangedIP = []

for x in userInput:
    if x == '.':
        defangedIP.append("[.]")
    else:
        defangedIP.append(x)

removeList =' '.join([str(i) for i in defangedIP])
print (removeList)

