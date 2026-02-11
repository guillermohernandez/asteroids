import pygame
import random
from circleshape import *
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            top_split = self.velocity.rotate(random_angle)
            bottom_split = self.velocity.rotate(-random_angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            chunk_un = Asteroid(self.position.x, self.position.y, new_radius)
            chunk_un.velocity = top_split * 1.2
            
            chunk_deux = Asteroid(self.position.x, self.position.y, new_radius)
            chunk_deux.velocity = bottom_split * 1.2