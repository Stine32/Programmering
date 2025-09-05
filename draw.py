import pygame

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

pygame.draw.line(screen, (0, 0, 0), (100, 380), (540, 380)) # Draw a black line

pygame.draw.line(screen, (0, 0, 0), (540, 380), (540, 100)) # Draw a black line

pygame.draw.line(screen, (0, 0, 0), (100, 380), (100, 100)) # Draw a black line

pygame.draw.line(screen, (0, 0, 0), (325, 10), (100, 100)) # Draw a black line

pygame.draw.line(screen, (0, 0, 0), (325, 10), (540, 100)) # Draw a black line

pygame.draw.line(screen, (0, 255, 0), (0, 381), (700, 381)) # Draw a green line

# Draw the ground
# Draw the bottom of the house
# Draw two walls
# Draw the roof

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears