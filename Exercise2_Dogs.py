class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking."

    def run_speed(self):
        return self.weight / (self.age * 10)

    def fight(self, other_dog):
        result = f" {self.name + " wins " +other_dog.name if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight else other_dog.name+' wins '+self.name} !"
        return result


def main():
    dog1 = Dog("Rex", 2, 10)
    dog2 = Dog("Karl", 3, 15)
    dog3 = Dog("Lama", 6, 20)
    print(dog1.bark())
    print(dog2.bark())
    print(dog1.fight(dog2))
    print(dog3.fight(dog1))
    print(dog3.fight(dog2))


if __name__ == "__main__":
    main()
