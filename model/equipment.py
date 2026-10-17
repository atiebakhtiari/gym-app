class Equipment:
    def __init__(self, equipment_id, name, condition):
        self.equipment_id = equipment_id
        self.name = name
        self.condition = condition

    # Equipment ID
    def get_equipment_id(self):
        return self.equipment_id

    def set_equipment_id(self, equipment_id):
        self.__equipment_id = GymValidator.validate_equipment_id(equipment_id)

    # Name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = GymValidator.validate_equipment_name(name)

    # Condition
    def get_condition(self):
        return self.__condition

    def set_condition(self, condition):
        self.__condition = GymValidator.validate_equipment_condition(condition)

    equipment_id = property(get_equipment_id, set_equipment_id)
    name = property(get_name, set_name)
    condition = property(get_condition, set_condition)

    def to_tuple(self):
        return (self.equipment_id, self.name, self.condition)

    def __repr__(self):
        return f"Equipment(equipment_id={self.equipment_id}, name={self.name}, condition={self.condition})"




