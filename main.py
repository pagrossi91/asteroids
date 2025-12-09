import sys
import pygame

from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Set up a group to hold and manage game objects
    updatable = pygame.sprite.Group() # this will hold all the objects that can be updated
    drawable = pygame.sprite.Group() # this will hold all the objects that can be drawn
    asteroids = pygame.sprite.Group() # this will hold all the asteroid objects
    shots = pygame.sprite.Group() # this will hold all the shot objects

    # Add game objects (which are the class instances) to groups
    Player.containers = (updatable, drawable) # adds Player instances to the updatable and drawable groups
    Asteroid.containers = (asteroids, updatable, drawable) # adds Asteroid instances to the asteroids, updatable, and drawable groups
    AsteroidField.containers = updatable # adds AsteroidField instances to the updatable group
    Shot.containers = (shots, updatable, drawable) # adds Shot instances to the shots, updatable, and drawable groups

    # Initialize an instance of player at the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Initialize the asteroid field
    asteroidfield = AsteroidField()

    while True:
        log_state()
        
        # Exit the game upon closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") # Make an entirely black window

        updatable.update(dt) # Update all updatable objects
        for asteroid in asteroids:
            if CircleShape.collides_with(asteroid, player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if CircleShape.collides_with(asteroid, shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        for sprite in drawable:
            sprite.draw(screen)  # Draw all drawable objects
        

        pygame.display.flip()
        dt = clock.tick(60)/1000 # limits frame rate to 60 FPS

if __name__ == "__main__":
    main()
