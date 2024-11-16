class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print("talk")


john = Person("John Smith")
print(john.name)
john.talk()
