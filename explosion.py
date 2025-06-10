import pygame
import random

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        if hasattr(self, "containers"):
            for container in self.containers:
                container.add(self)

        self.x = x
        self.y = y
        self.particles = []
        self.lifetime = 30  # frames the explosion lasts
        self.age = 0

        # Create particles for the explosion
        for _ in range(10):  # 10 particles
            particle = {
                'x': x,
                'y': y,
                'vx': random.uniform(-3, 3),  # random velocity
                'vy': random.uniform(-3, 3),
                'color': random.choice([(255, 100, 0), (255, 200, 0), (255, 255, 255)])
            }
            self.particles.append(particle)

    def update(self, dt):  # Accept dt parameter like other sprites
        self.age += 1
        # Update each particle position
        for particle in self.particles:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            # Slow down particles over time
            particle['vx'] *= 0.95
            particle['vy'] *= 0.95

        # Remove explosion when lifetime expires
        if self.age >= self.lifetime:
            self.kill()  # Remove from all sprite groups

    def draw(self, screen):
        for particle in self.particles:
            # Make particles fade out over time
            alpha = max(0, 255 - (self.age * 8))
            pygame.draw.circle(screen, particle['color'],
                             (int(particle['x']), int(particle['y'])), 3)
