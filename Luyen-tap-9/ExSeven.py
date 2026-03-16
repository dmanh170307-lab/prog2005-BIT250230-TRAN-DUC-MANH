class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
    @classmethod
    def from_string(cls, chuoi_du_lieu):
        ten, tuoi = chuoi_du_lieu.split("-")
        return cls(ten, tuoi)
nguoi_1 = Person.from_string("Nam-20")
print(nguoi_1.name)