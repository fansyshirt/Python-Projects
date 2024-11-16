import re

pattern = r"spam"
text = input("> enter text")

match = re.search(pattern, text)
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
else:
    print("'spam' was not not found")
