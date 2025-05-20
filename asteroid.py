import pygame
import constants
from circleshape import CircleShape





class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def update(self, dt):
        self.pos = self.pos + self.velocity * dt


    def draw(self, surface):
        pygame.draw.circle(surface, "white", tuple(map(int, self.pos)), self.radius, 2) 
