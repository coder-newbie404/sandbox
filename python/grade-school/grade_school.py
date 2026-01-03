class School:
    def __init__(self):
        self.roster_dict = {}
        self.added_list = []

    def add_student(self, name, grade):
        if name in self.roster_dict:
            self.added_list.append(False)
        else:
            self.added_list.append(True)
            self.roster_dict[name] = grade

    def roster(self):
        sorted_roster = sorted(self.roster_dict.items(), key=lambda item: (item[1], item[0]))
        return [name for name, grade in sorted_roster]

    def grade(self, grade_number):
        grades = [name for name, grade in self.roster_dict.items() if grade == grade_number]
        return sorted(grades)

    def added(self):
        return self.added_list