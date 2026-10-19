from tools.validation import GymValidator

class WorkSession:
    def __init__(self, session_id, session_date, duration, member, trainer, equipment, exercise_name, sets_reps):
        self.session_id = session_id
        self.session_date = session_date
        self.duration = duration
        self.member = member
        self.trainer = trainer
        self.equipment = equipment
        self.exercise_name = exercise_name
        self.sets_reps = sets_reps

    # Session ID
    def get_session_id(self):
        return self.__session_id

    def set_session_id(self, session_id):
        self.__session_id = GymValidator.validate_session_id(session_id)

    # Exercise Name
    def get_exercise_name(self):
        return self.__exersize_name

    def set_exercise_name(self, exercise_name):
        self.__exercise_name = GymValidator.validate_exercise_name(exercise_name)

    session_id = property(get_session_id, set_session_id)
    exercise_name = property(get_exercise_name, set_exercise_name)


    def to_tuple(self):
        return (
            self.session_id,
            self.session_date,
            str(self.member),
            str(self.trainer),
            str(self.equipment),
            self.exercise_name,
            self. sets_re,
            self.duration
        )

    def __repr__(self):
        return (
            f"WorkoutSession(session_id={self.session_id}, member={self.member}, "
            f"trainer={self.trainer}, equipment={self.equipment}, "
            f"exercise={self.exercise_name}, sets_reps={self.sets_reps})"
        )
