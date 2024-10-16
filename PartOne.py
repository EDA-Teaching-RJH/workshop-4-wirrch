userInput = input("Name of variable in camelCase: ")
newString = ""

for c in userInput:
    if c == c.upper():
        newString += f"_{c.lower()}"
    else:
        newString += c

print(newString)

