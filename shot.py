"""
Defines a shot class, inherited from CircleShape
"""

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    """
    Override the draw() method to draw the shot using the pygame.draw.circle function. It accepts:
    The "surface" to draw on (the screen object)
    The color of the circle ("red")
    Its own position as the center
    Its own radius
    The width of the line to draw the circle (use LINE_WIDTH from constants.py)
    """
    def draw(self, screen):
        color = "red"
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    """
    Override the update() method so that it moves in a straight line at constant speed. 
    On each frame, it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
    """
    def update(self, dt):
        self.position += self.velocity * dt
    
