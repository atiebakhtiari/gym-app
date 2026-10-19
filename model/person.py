from tools.validation import GymValidator

class Person:
    def __init__(self, person_id, name, family, age, phone, bmi):
        self.person_id = person_id
        self.name = name
        self.family = family
        self.age = age
        self.phone = phone
        self.bmi = bmi

    # Age
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = GymValidator.validate_age(age)

    # Name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = GymValidator.validate_name(name)

    # Family
    def get_family(self):
        return self.__family
    def set_family(self, family):
        self.__family = GymValidator.validate_family(family)

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
    name = property(get_name, set_name)
    family = property(get_family, set_family)
    phone = property(get_phone, set_phone)
    bmi = property(get_bmi, set_bmi)

    def to_tuple(self):
        return (self.person_id, self.name, self.family, self.age, self.phone, self.bmi)

    def __repr__(self):
        return f"Person(person_id={self.person_id}, name={self.name}, family={self.family}, age={self.age}, phone={self.phone}, bmi={self.bmi})"