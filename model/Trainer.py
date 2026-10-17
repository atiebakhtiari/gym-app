from model.person import Person

class Trainer(Person):
    def __init__(self, person_id, name, age, phone, bmi, specialization):
        super().__init__(person_id, name, age, phone, bmi)
        self.specialization = specialization

    def assign_workout(self, member_name, workout_name):
        return f"Trainer {self.name} assigned {workout_name} to {member_name}"

    def to_tuple(self):
        return (self.person_id, self.name, self.age, self.phone, self.bmi, self.specialization)

    def __repr__(self):
        return f"Trainer(person_id={self.person_id}, name={self.name}, specialization={self.specialization})"
