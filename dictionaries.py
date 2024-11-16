#name: John Smith
#email: john@gmail.com
#phone: 04040404040404
#ect.

customer = {
    "name": "John Smith",
    "age": "30",
    "is_verified": True
}

print (customer["name"])


phone = input("Phone No: ")
digits = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",	
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

output = ""

for ch in phone:
    output += digits.get(ch, "!") + " "
print(output)
