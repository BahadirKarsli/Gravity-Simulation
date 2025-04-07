import pygame
import numpy as np
from menu import get_user_input
from simulation import run_simulation

# Pygame start
pygame.init()

# Screen and constants
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulation")

# Main loop
running = True
while running:
    # get user input for simulation parameters
    center_mass, center_size, particle_mass, particle_count = get_user_input()

    # Simulation start
    should_restart = run_simulation(screen, WIDTH, HEIGHT, center_mass, center_size, particle_mass, particle_count)

    # Check if the user wants to restart the simulation
    if not should_restart:
        running = False

pygame.quit()
