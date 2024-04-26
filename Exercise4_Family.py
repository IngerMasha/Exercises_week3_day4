class Family:
    def __init__(self, last_name):
        self.members = []
        self.last_name = last_name

    def born(self, **kwargs):
        for name, age in kwargs.items():
            self.members.append({"name": name, "age": age, "is_child": True})
        print("Congratulations to the family!")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] >= 18:
                    return True
                else:
                    return False
        return False
    def family_presentation(self):
        print(f"Family {self.last_name}:")
        for member in self.members:
            print(
                f"Name: {member['name']}, Age: {member['age']}, Gender: {member.get('gender', 'Unknown')}, Is Child: {member['is_child']}")
def main():
    my_family = Family("Black")
    my_family.members.extend([
        {'name': 'Sirius', 'age': 35, 'gender': 'Male', 'is_child': False},
        {'name': 'Regulus', 'age': 32, 'gender': 'Male', 'is_child': False},
        {'name': 'Bellatrix', 'age': 38, 'gender': 'Female', 'is_child': False},
        {'name': 'Andromeda', 'age': 40, 'gender': 'Female', 'is_child': False}
    ])
    my_family.born(Nymphadora=0)
    print(my_family.is_18("Sirius"))
    print(my_family.is_18("Nymphadora"))
    my_family.family_presentation()
if __name__=="__main__":
    main()


