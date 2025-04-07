import pygame
from particle import MassiveObject, Particle
import numpy as np

def run_simulation(screen, WIDTH, HEIGHT, center_mass_value, center_size_value, particle_mass_value, particle_count_value):
    center_mass = MassiveObject(WIDTH // 2, HEIGHT // 2, center_mass_value, center_size_value)
    particles = [Particle(np.random.randint(100, 700), np.random.randint(100, 500), particle_mass_value) for _ in range(particle_count_value)]

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return True  # Back to menu

        center_mass.draw(screen)
        for p in particles:
            p.update(center_mass)
            p.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    return False
