class Flower:
    def __init__(self):
        self._color = ""

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color
hoa = Flower()
hoa.set_color("Đỏ")
print(f"Màu sắc của hoa: {hoa.get_color()}")