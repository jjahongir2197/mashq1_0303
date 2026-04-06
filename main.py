class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores)/len(self.scores) if self.scores else 0

    def info(self):
        print(f"{self.name}, {self.age} y.o, Average: {self.avg()}")

def student_demo():
    s1 = Student("Ali", 18)
    s2 = Student("Vali", 19)
    s1.add_score(80)
    s1.add_score(90)
    s2.add_score(70)
    s2.add_score(85)
    s1.info()
    s2.info()

student_demo()
