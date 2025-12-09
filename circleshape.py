"""
Pre-built script from boot.dev
This class inherits from pygame's base class Shape sprite. All objects in our game will represented as circles for collision purposes.
We store 3 additional attributes specific to our game:
- position (x and y coordinates)
- velocity
- radius
"""

import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        min_distance = self.radius + other.radius
        return pygame.Vector2.distance_to(self.position, other.position) <= min_distance
        