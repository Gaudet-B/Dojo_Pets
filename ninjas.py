from pets import Pet, Cat, Dog

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        self.pet.play()
    def feed(self):
        self.pet.eat()
    def bathe(self):
        self.pet.noise()

dolce = Cat('Dolce', 'cat', 'treat bowling')
brian = Ninja('Brian', 'Gaudet', 'greenies', 'Natural Balance', dolce)

brian.feed()
brian.walk()
brian.bathe()