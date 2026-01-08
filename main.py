import sys
import pygame
import player
from asteroid import Asteroid
import asteroidfield
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from  logger import log_state, log_event
import shot

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
        
    # Initialize Game Clock
    clock = pygame.time.Clock()
    dt = 0

    # create instance groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # instanciate objects, set their containers
    asteroidfield.AsteroidField.containers = (updatable)
    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    shot.Shot.containers = (updatable, drawable, shots)
    p1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = asteroidfield.AsteroidField()
    

    # Game Loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(p1):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for s1 in shots:
                if asteroid.collides_with(s1):
                    log_event("asteroid_shot")
                    asteroid.split()
                    s1.kill()
                    
        screen.fill("black")
        for shape in drawable:
            shape.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
