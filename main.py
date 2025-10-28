import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    space = AsteroidField()

    dt = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        for object in asteroids:
            if player.collide(object):
                print("Game over!")
                running = False

        screen.fill((0,0,0))

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        # it has to do with the framerate
        dt = clock.tick(60) / 1000

    return

if __name__ == "__main__":
    main()
    
