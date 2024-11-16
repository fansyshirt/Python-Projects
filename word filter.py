command = input("> ")
word = command.split(' ')
heresy = 0

emojis = {
    "word1": "`",
    "word2": "`",
    "word3": "`",
    "word4": "`",
    "word5": "`",
    "word6": "`",
    "word6": "`",
    "word7": "`",
    "word8": "`",
    "word9": "`"
}

output = ""

for word in word:
    output += emojis.get(word, word) + " "
for word in output:
    if word == "`":
        heresy = 1
        break
if heresy == 0:
    print(output)
if heresy == 1:
    print("NO")
