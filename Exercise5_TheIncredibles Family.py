from Exercise4_Family import Family

class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] >= 18:
                    print(f"{member["name"]}'s power is: {member["power"]}")
                else:
                    raise Exception(f"{member["name"]} is not over 18 years old.")

    def incredible_presentation(self):
        print("*Here is our powerful family*")
        super().family_presentation()
def main():
    the_incredibles_family = TheIncredibles("Incredibles")
    the_incredibles_family.members.extend([
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly',
         'incredible_name': 'MikeFly'},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds',
         'incredible_name': 'SuperWoman'}
    ])
    the_incredibles_family.incredible_presentation()
    the_incredibles_family.born(BabyJack=0)
    the_incredibles_family.incredible_presentation()
    try:
        the_incredibles_family.use_power('Michael')
    except Exception as e:
        print(f"Exception occurred: {e}")
    try:
        the_incredibles_family.use_power('BabyJack')
    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__=="__main__":
    main()