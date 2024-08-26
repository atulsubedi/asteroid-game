import sys
import pygame
from constants import *
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    b = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Shot.containers = (shot, updatable, drawable)



    Player.containers = (updatable, drawable)
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    Asteroid.containers = (asteroid, drawable, updatable)
    AsteroidField.containers = (updatable)
    asf = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)

        for obj in asteroid:
            if obj.check_collision(p):
                print("Game over!")
                sys.exit()
            for s in shot:
                if obj.check_collision(s):
                 s.kill()
                 obj.split()


        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = b.tick(60) / 1000



if __name__ == "__main__":
    main()
