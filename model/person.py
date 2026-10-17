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
        if not isinstance(age, int) or age < 0 or age > 120:
            raise ValueError("Invalid age !!!")
        self.__age = age

    # Phone
    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        if not isinstance(phone, int) or phone <= 0:
            raise ValueError("Invalid phone !!!")
        self.__phone = phone

    # BMI
    def get_bmi(self):
        return self.__bmi

    def set_bmi(self, bmi):
        if not isinstance(bmi, (int, flaot)) or bmi < 10 or bmi > 60:
            raise ValueError("Invalid bmi !!!")
        self.__bmi = bmi


    age = property(get_age, set_age)
    phone = property(get_phone, set_phone)
    bmi = property(get_bmi, set_bmi)

    def to_tuple(self):
        return (self.person_id, self.name, self.age, self.phone, self.bmi)

    def __repr__(self):
        return f"Person(person_id={self.person_id}, name={self.name}, age={self.age}, phone={self.phone}, bmi={self.bmi})"