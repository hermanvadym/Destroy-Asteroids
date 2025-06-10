import pygame
from constants import *

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
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius


    def wrap_around_screen(self):
    	if self.position.x > SCREEN_WIDTH:
        	self.position.x = 0
    	elif self.position.x < 0:
        	self.position.x = SCREEN_WIDTH

    	if self.position.y > SCREEN_HEIGHT:
        	self.position.y = 0
    	elif self.position.y < 0:
        	self.position.y = SCREEN_HEIGHT
