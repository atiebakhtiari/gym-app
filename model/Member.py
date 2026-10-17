from model.person import Person

class Member(Person):
    def __init__(self, person_id, name, age, phone, bmi, class_level):
        super().__init__(person_id, name, age, phone, bmi)
        self.class_level = class_level

    def check_in(self):
        return f"Member {self.name} checked in successfully."

    def to_tuple(self):
        return (self.person_id, self.name, self.age, self.phone, self.bmi, self.class_level)

    def __repr__(self):
        return f"Member(person_id={self.person_id}, name={self.name}, class_level={self.class_level})"