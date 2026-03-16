class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Động vật đang kêu...")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print(f"Chó {self.name} kêu:gâu gâu")
cho_con = Dog("trminh")
cho_con.sound()