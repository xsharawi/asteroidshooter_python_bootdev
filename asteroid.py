import random
from typing import override

import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    @override
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    @override
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        ran = random.uniform(20, 50)
        v1 = self.velocity.rotate(ran)
        v2 = self.velocity.rotate(-ran)
        newRad = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, newRad)
        a1.velocity = v1 * 1.2
        a2 = Asteroid(self.position.x, self.position.y, newRad)
        a2.velocity = v2 * 1.2
