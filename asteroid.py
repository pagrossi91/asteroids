"""
Defines an asteroid class, inherited from CircleShape
"""

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    """
    Override the draw() method to draw the asteroid using the pygame.draw.circle function. It accepts:
    The "surface" to draw on (the screen object)
    The color of the circle ("white")
    Its own position as the center
    Its own radius
    The width of the line to draw the circle (use LINE_WIDTH from constants.py)
    """
    def draw(self, screen):
        color = "white"
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    """
    Override the update() method so that it moves in a straight line at constant speed. 
    On each frame, it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
    """
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # The print statements were helpful with troubleshooting. Keeping them for posterity.
        # print(f"Dead asteroid: radius = {self.radius}, velocity: {self.velocity}")
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            # print(f"New asteroid radius: {new_asteroid_radius}")

            asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid1.velocity = self.velocity.rotate(angle) * 1.2
        
            asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid2.velocity = self.velocity.rotate(-angle) * 1.2
            
            # print(f"Asteroid 1: radius = {asteroid1.radius}, velocity: {asteroid1.velocity}")
            # print(f"Asteroid 2: radius = {asteroid2.radius}, velocity: {asteroid2.velocity}")
            # print("End of split")
            # print("")