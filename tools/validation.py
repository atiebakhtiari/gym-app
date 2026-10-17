class GymValidator:
    @staticmethod
    def validate_age(age):
        if not isinstance(age, int) or age <= 0 or age > 120:
            raise ValueError("Age Invalid !!!")
        return age

    @staticmethod
    def validate_phone(phone):
        if not isinstance(phone, int) or phone <= 0:
            raise ValueError("Phone Invalid !!!")
        return phone

    @staticmethod
    def validate_bmi(bmi):
        if not isinstance(bmi, (int, float)) or bmi < 10 or bmi > 60:
            raise ValueError("BMI Invalid !!!")
        return bmi

    @staticmethod
    def validate_equipment_id(equipment_id):
        if not isinstance(equipment_id, int) or equipment_id <= 0:
            raise ValueError("Equipment Id Invalid !!!")
        return equipment_id

    @staticmethod
    def validate_equipment_name(name):
        if not name or not isinstance(name, str):
            raise ValueError("Equipment Name Invalid !!!")
        return name

    @staticmethod
    def validate_equipment_condition(condition):
        if not condition or not isinstance(condition, str):
            raise ValueError("Equipment Condition Invalid !!!")
        return condition
