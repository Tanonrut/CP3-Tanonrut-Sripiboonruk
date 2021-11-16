userSelect = int(input("Please select your number >>> "))
text = "*"
print(" " * userSelect, text)
for x in range(userSelect):
    for y in range(2):
        text += "*"
    print(" "*(userSelect-(x+1)), text)