class Human:
    def __init__(self, id_number, name, age, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = True
        self.blood_type = blood_type
        self.family = []
    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)

class Queue:
    def __init__(self):
        self.human = []
    def add_person(self, person):
        if person.age >= 60 or person.priority == True:
            self.human.insert(0, person)
        else:
            self.human.append(person)

    def find_in_queue(self, person):
        if person in self.human:
            return self.human.index(person)
        else:
            print("This person is not in the list.")
            return None

    def swap(self, person1, person2):
        index1 = self.human.index(person1)
        index2 = self.human.index(person2)
        self.human[index1], self.human[index2] = self.human[index2], self.human[index1]

    def get_next(self):
        return self.human[0]

    def get_next_blood_type(self, blood_type):
        for person in self.human:
            if person.blood_type == blood_type:
                return person
        return None

    def sort_by_age(self):
        self.human.sort(key=lambda x: (not x.priority, x.age))

        # self.human.sort(key=lambda x: (not x.priority, x.age, self.human.index(x)))

    def rearrange_queue(self):
        if len(self.human) <= 1:
            return

        i = 0
        while i < len(self.human) - 1:
            current_person = self.human[i]
            next_person = self.human[i + 1]
            if current_person.family and current_person.family[0] == next_person:
                # If the next person is a family member of the current person, move the next person forward
                self.human.insert(i + 1, self.human.pop(i))
                i -= 1  # Rewind i to check again after rearrangement
            i += 1

def main():
    person1 = Human(1, "Alice", 25, "A")
    person2 = Human(2, "Bob", 65, "B")
    person3 = Human(3, "Charlie", 70, "O")
    person4 = Human(4, "David", 40, "AB")

    queue = Queue()

    queue.add_person(person1)
    queue.add_person(person2)
    queue.add_person(person3)
    queue.add_person(person4)

    print("Initial queue:")
    for person in queue.human:
        print(person.name, person.age, person.blood_type)

    queue.sort_by_age()
    print("\nQueue sorted by age:")
    for person in queue.human:
        print(person.name, person.age, person.blood_type)

    queue.rearrange_queue()

    print("\nQueue after rearrangement:")
    for person in queue.human:
        print(person.name, person.age, person.blood_type)


if __name__=="__main__":
    main()