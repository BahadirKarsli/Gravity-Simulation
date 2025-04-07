import pygame
import time
import os

# Pygame start
pygame.init()

# screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulation")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
GRAY = (200, 200, 200)

FONT_PATH = os.path.join("fonts", "Quicksand-Light.ttf")

TITLE_FONT = pygame.font.Font(FONT_PATH, 48) 
LABEL_FONT = pygame.font.Font(FONT_PATH, 32)  
INPUT_FONT = pygame.font.Font(FONT_PATH, 28) 
BUTTON_FONT = pygame.font.Font(FONT_PATH, 28) 

class InputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.text = text
        self.active = False
        self.font = INPUT_FONT 
        self.cursor_visible = True
        self.cursor_timer = time.time()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.active = False
            else:
                self.text += event.unicode

    def draw(self, screen):
        # draw box
        pygame.draw.rect(screen, self.color, self.rect, 2)
        # draw text
        text_surface = self.font.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        # draw cursor
        if self.active:
            if time.time() - self.cursor_timer > 0.5:  # toggle cursor visibility every 0.5 seconds
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = time.time()
            if self.cursor_visible:
                text_width = text_surface.get_width()
                cursor_x = self.rect.x + 5 + text_width
                pygame.draw.line(screen, WHITE, (cursor_x, self.rect.y + 5), (cursor_x, self.rect.y + self.rect.height - 5), 2)

# Button class
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BLUE
        self.text = text
        self.action = action
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = BUTTON_FONT.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return self.action()
        return None

# user input boxes
center_mass_box = InputBox(300, 210, 250, 40, "1000")
center_size_box = InputBox(300, 260, 250, 40, "100")
particle_mass_box = InputBox(300, 310, 250, 40, "1")
particle_count_box = InputBox(300, 360, 250, 40, "10")

input_boxes = [center_mass_box, center_size_box, particle_mass_box, particle_count_box]

# create button
start_button = Button(310, 450, 230, 50, "Start Simulation", lambda: (
    float(center_mass_box.text), int(center_size_box.text),
    float(particle_mass_box.text), int(particle_count_box.text)
))

def get_user_input():
    running = True
    while running:
        screen.fill(BLACK)
        
        title_surface = TITLE_FONT.render("Gravity Simulation", True, WHITE)
        screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 50))


        labels = ["Center Mass:", "Center Size:", "Particle Mass:", "Particle Count:"]
        
        for i, label in enumerate(labels):
            text_surface = LABEL_FONT.render(label, True, WHITE)
            screen.blit(text_surface, (50, 210 + i * 50))
        
        for box in input_boxes:
            box.draw(screen)
        
        start_button.draw(screen)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            for box in input_boxes:
                box.handle_event(event)
            result = start_button.handle_event(event)
            if result:
                return result

if __name__ == "__main__":
    values = get_user_input()
    print("Inputs:", values)