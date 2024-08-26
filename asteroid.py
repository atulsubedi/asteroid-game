import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white",  self.position, self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        blueAngel = random.uniform(20, 50)
        a = self.velocity.rotate(blueAngel)
        b = self.velocity.rotate(-blueAngel)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, newRadius)
        asteroid.velocity = a * 1.3
        asteroid = Asteroid(self.position.x, self.position.y, newRadius)
        asteroid.velocity = b * 1.3
