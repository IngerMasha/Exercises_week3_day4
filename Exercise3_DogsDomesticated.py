import random

from Exercise2_Dogs import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        self.name = name
        self.age = age
        self.weight = weight
        self.trained = trained

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *dog_names):
        dog_names_str = ", ".join(dog_names)
        print(f"{dog_names_str} all play together.")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            trick = random.choice(tricks)
            print(trick)
        else:
            print(f"{self.name} is not trained to do tricks.")


def main():
    dog1 = PetDog("Rex", 2, 10)
    dog2 = PetDog("Karl", 3, 15)
    dog3 = PetDog("Lama", 6, 20)
    dog1.train()
    dog3.train()
    dog1.play(dog3.name, dog2.name)
    dog3.do_a_trick()
    dog2.do_a_trick()


if __name__ == "__main__":
    main()
