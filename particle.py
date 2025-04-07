import numpy as np
import pygame

G = 0.1  # Gravitational constant for simulation

# Center Object
class MassiveObject:
    def __init__(self, x, y, mass, size):
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = size
        self.image = pygame.image.load("images/center2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (2*size, 2*size))  # 
    
    def draw(self, screen):
        screen.blit(self.image, (int(self.x - self.radius), int(self.y - self.radius)))


# Particle class
class Particle:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = 6
        self.vx = np.random.uniform(-1, 1)
        self.vy = np.random.uniform(-1, 1)
        
    def update(self, center):
        dx = center.x - self.x
        dy = center.y - self.y
        r = np.hypot(dx, dy)

        if r > 5:  # a limit so that the attraction is not too large.
            force = G * (self.mass * center.mass) / (r ** 2)
            ax = force * dx / r  # force into components
            ay = force * dy / r

            self.vx += ax
            self.vy += ay

            self.x += self.vx
            self.y += self.vy

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
