class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print(f"sv {self.name} có điểm là {self.score}")

student1 = Student("A", 10)
student1.display()