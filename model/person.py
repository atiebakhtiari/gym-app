class Person:
    def __init__(self, name, age, phone, bmi):
        self.name = name
        self.age = age
        self.phone = phone
        self.bmi = bmi

    def get_info(self):
        return {
            "name": self.name,
            "age": self.age,
            "phone": self.phone,
            "bmi": self.bmi
        }

    def set_info(self, name, age, phone, bmi):
        self.name = name
        self.age = age
        self.phone = phone
        self.bmi = bmi

    def __repr__(self):
        return (f"name: {self.name}, age: {self.age}, phone: {self.phone}, bmi: {self.bmi}")