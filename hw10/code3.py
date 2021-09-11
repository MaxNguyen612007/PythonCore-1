 class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def eat(self):
        if self.is_hungry:
            self.is_hungry = False
        else:
            print(f"{self.name} is not hungry!")

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'


class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Pet:
    def __init__(self, my_dogs):
        self.my_dogs = my_dogs

    def status(self):
        have_eaten = True
        print("My dogs are hungry.")
        for dog in self.my_dogs:
            if dog.is_hungry:
                have_eaten = False
                dog.eat()
        
        if have_eaten:
            print("My dogs are not hungry.")
            for dog in self.my_dogs:
                dog.is_hungry = True
    
    def __str__(self):
        dog_string = ""
        dog_string += f"I have {len(self.my_dogs)} dogs. "
        for dog in self.my_dogs:
            dog_string += f"{dog.name} is {dog.age} years old. "
        dog_string += "And they are mammals, of course."
        return dog_string

pets = Pet([Dog("Tom", 6), Dog("Jerry", 9), Dog("Butt", 3), Dog("Wine", 1)])
print(pets)
pets.status()



