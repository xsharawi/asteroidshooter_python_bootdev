from typing import override
import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.bullet_limit = 0

    @override
    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float):
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt: float):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def update(self, dt: float):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.rotate(-dt)
        if keys[pygame.K_f]:
            self.move(dt)
        if keys[pygame.K_p]:
            self.move(-dt)
        if keys[pygame.K_b]:
            self.shoot()
        self.bullet_limit -= dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def shoot(self):
        if self.bullet_limit > 0:
            return
        t: pygame.Vector2 = self.position
        shot = Shot(t.x, t.y, self.radius)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.bullet_limit = PLAYER_SHOOT_COOLDOWN_SECONDS
