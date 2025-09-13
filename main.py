import pygame
from libs.Particle import Particle
from libs.Constrain import ConstrainHandler


class App:
    def __init__(self):
        self.Width = 500
        self.Height = 500
        self.Status = 'running'
        self.FPS = 120
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.Width, self.Height))
        self._initalize_()

    def _initalize_(self):
        self.CH = ConstrainHandler()
        self.cloth = pygame.math.Vector2(30, 30)
        self.size = 10
        self.anchors = {
                "indexies": [0, 9*int(self.cloth.y), 19*int(self.cloth.y), 29*int(self.cloth.y)],
                "cords": []
                   }
        self.particles = []
        for x in range(int(self.cloth.x)):
            for y in range(int(self.cloth.y)):
                self.particles.append(Particle(10 + x * self.size, 10 + y * self.size))
                if x + y*self.cloth.y in self.anchors["indexies"]:
                    self.anchors["cords"].append((10 + y * self.size, 10 + x * self.size))
        self.constrains = []
        for j in range(int(self.cloth.x)):
            for i in range(0, int(self.cloth.y) - 1):
                self.constrains.append((self.particles[i+j*int(self.cloth.y)], self.particles[i+j*int(self.cloth.y)+1], self.size))
        for j in range(int(self.cloth.x)-1):
            for i in range(0, int(self.cloth.y)):
                self.constrains.append((self.particles[i+j*int(self.cloth.y)], self.particles[i+j*int(self.cloth.y)+int(self.cloth.y)], self.size))

    def run(self):
        while (self.Status == 'running'):
            MousePosition = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Status = 'close'
            self.display.fill((15, 15, 15))
            for i in range(len(self.anchors['indexies'])):
                self.particles[self.anchors['indexies'][i]].accelaration = pygame.math.Vector2(self.anchors['cords'][i]) - self.particles[self.anchors['indexies'][i]].position
            for constrain in self.constrains:
                self.CH.update(constrain, self.display)
            for i, p in enumerate(self.particles):
                if (p.position - MousePosition).magnitude() < 10:
                    p.velocity.y -= 10
                p.update()
                # p.draw(self.display, (255, 255, 255))
            pygame.display.update()
            self.clock.tick(self.FPS)
        quit()


if __name__ == "__main__":
    game = App()
    game.run()
