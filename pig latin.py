command = input("enter you text to be converted to pig latin\n")

command_list = command.split(" ")
word_list = []
for word in command_list:
    iterate = 0
    word = ""
    f_letter = ""
    for item in word:
        iterate += 1
        if iterate == 1:
            f_letter = item
        elif iterate > 1 and iterate < len(word) - 1:
            word += item
        else:
            word += item
            word_list.append(word + f_letter)
print(word_list)
