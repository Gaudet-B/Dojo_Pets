class Pet:
    def __init__(self, name , type , tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 100
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health += 5
    def noise(self):
        print('insert pet noise...')

class Cat(Pet):
    def __init__(self, name , type , tricks):
        super().__init__(name , type , tricks)
        self.sound = 'meow!'
    def noise(self):
        print(self.sound)


class Dog(Pet):
    def __init__(self, name , type , tricks):
        super().__init__(name , type , tricks)
        self.sound = 'woof!'
    def noise(self):
        print(self.sound)