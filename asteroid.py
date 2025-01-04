import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.is_crashed = False

    def draw(self, screen):
        if self.is_crashed:
            pygame.draw.circle(screen, "red", self.position, self.radius, 4)
            return
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        deviation = random.uniform(50, 20)
        radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, radius)
        ast1.velocity = self.velocity.rotate(deviation)
        ast1.velocity *= 1.2

        ast2 = Asteroid(self.position.x, self.position.y, radius)
        ast2.velocity = self.velocity.rotate(-deviation)
        ast2.velocity *= 1.2
        return [
            ast1,
            ast2,
        ]
