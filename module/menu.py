class MainMenu:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Hello my name is " + self.name)

p1 = MainMenu("John", 36)

p1.show()
