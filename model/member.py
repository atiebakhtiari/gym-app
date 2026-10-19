from model.person import Person

class Member(Person):
    def __init__(self, person_id, name, family, age, phone, bmi, class_level):
        super().__init__(person_id, name, family, age, phone, bmi)
        self.class_level = class_level

    def check_in(self):
        return f"Member {self.name} {self.family} checked in successfully."

    def to_tuple(self):
        return (self.person_id, self.name, self.family, self.age, self.phone, self.bmi, self.class_level)

    def __repr__(self):
        return f"Member(person_id={self.person_id}, name={self.name}, family={self.family}, class_level={self.class_level})"
