import pygame
import circleshape
import player
import asteroid
import asteroidfield


from constants import *

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()



player.Player.containers = (updateable, drawable)  
asteroid.Asteroid.containers = (asteroids, updateable, drawable)
asteroidfield.AsteroidField.containers = (updateable,)
asteroidfield.AsteroidField()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player_ship = player.Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        screen.fill("black") 
        updateable.update(dt)
        for thing in drawable:
                thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    main()

