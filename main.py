import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_state, log_event
from player import Player
from shot import Shot


def main():
    _ = pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = updatables
    Shot.containers = (shots, updatables, drawables)
    plr = Player(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
    af = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        _ = screen.fill("black")
        dt = clock.tick(60) / 1000
        for d in drawables:
            d.draw(screen)
        updatables.update(dt)
        for a in asteroids:
            if plr.collides_with(a):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()


if __name__ == "__main__":
    main()
