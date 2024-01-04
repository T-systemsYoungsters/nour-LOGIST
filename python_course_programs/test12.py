class Animal():
    def __init__(self):
        self.name=""
        print("An new animal has been born.")

    def eat(self):
        print("Munch munch.")
    
    def make_noise(self,):
        print("Grrr says",self.name)


class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("A cat has been born")

    def make_noise(self):
        print("Meow says",self.name)
    

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("A dog has been born.")
        
    def make_noise(self):
        print("Bark says",self.name)

cat = Cat()
cat.name = "Molly"
cat.eat()
cat.make_noise()

dog1 =Dog()
dog1.name = "Rocky"
dog1.eat()
dog1.make_noise()

dog2 =Dog()
dog2.name = "Ruby"
dog2.eat()
dog2.make_noise()


animal = Animal()
animal.name = "Daisy"
animal.eat()
animal.make_noise()

    


        