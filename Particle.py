from pygame.math import Vector2
from pygame.draw import circle


class Particle:
    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.velocity = Vector2()
        self.accelaration = Vector2(0, 0.1)

    def update(self):
        self.velocity += self.accelaration
        self.position += self.velocity

    def draw(self, surface, color):
        circle(surface, color, self.position, 3)
