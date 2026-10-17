from tools.validation import GymValidator

class Person:
    def __init__(self, person_id, name, age, phone, bmi):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.phone = phone
        self.bmi = bmi

    # Age
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = GymValidator.validate_age(age)

    # Phone
    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = GymValidator.validate_phone(phone)

    # BMI
    def get_bmi(self):
        return self.__bmi

    def set_bmi(self, bmi):
        self.__bmi = GymValidator.validate_bmi(bmi)


    age = property(get_age, set_age)
    phone = property(get_phone, set_phone)
    bmi = property(get_bmi, set_bmi)

    def to_tuple(self):
        return (self.person_id, self.name, self.age, self.phone, self.bmi)

    def __repr__(self):
        return f"Person(person_id={self.person_id}, name={self.name}, age={self.age}, phone={self.phone}, bmi={self.bmi})"