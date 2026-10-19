from model.person import Person

class Trainer(Person):
    def __init__(self, person_id, name, family, age, phone, bmi, specialization):
        super().__init__(person_id, name, family, age, phone, bmi)
        self.specialization = specialization

    def assign_workout(self, member_name, member_family, workout_name):
        return f"Trainer {self.name} {self.family} assigned {workout_name} to {member_name} {member_family}"

    def to_tuple(self):
        return (self.person_id, self.name, self.family, self.age, self.phone, self.bmi, self.specialization)

    def __repr__(self):
        return f"Trainer(person_id={self.person_id}, name={self.name}, family={self.family}, specialization={self.specialization})"
