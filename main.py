import sys
import pygame
from constants import *
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    score = 0
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
        font = pygame.font.Font(None, 36)
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
                    score += 10
                    s.kill()
                    obj.split()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        dt = b.tick(60) / 1000


if __name__ == "__main__":
    main()
