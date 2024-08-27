class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Скорость не может быть меньше или равна 0!")

    def count_moves(self, x2, y2):
        x_distance = abs(x2 - self.x)
        y_distance = abs(y2 - self.y)

        x_moves = (x_distance + self.s - 1) // self.s
        y_moves = (y_distance + self.s - 1) // self.s

        return x_moves + y_moves

turtle = Turtle()

turtle.go_up()
turtle.go_right()
print(f"Текущая позиция: ({turtle.x}, {turtle.y})")

turtle.evolve()
print(f"Скорость черепашки: {turtle.s}")

moves_needed = turtle.count_moves(5, 5)
print(f"Минимальное количество шагов до (5, 5): {moves_needed}")

try:
    turtle.degrade()
    turtle.degrade()
except ValueError as e:
    print(e)