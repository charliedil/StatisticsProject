class Student:
    def __init__(self, id, sex, teacher, status, score):
        self.id = id
        self.sex = sex
        self.teacher = teacher
        self.status = status
        self.score = score

    def __repr__(self):
        out = str.format("Student ID: {}\nStudent sex: {}\nStudent teacher: {}\nStudent status: {}\nStudent score: "
                         "{}", self.id, self.sex, self.teacher, self.status, self.score)
        return out
