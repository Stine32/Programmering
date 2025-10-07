import pygame
import math
import datetime
import sys

pygame.init()

#Opretter vindue af 640x480 pixels + navn + pygame clock til tiden
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Analogt ur")
clock = pygame.time.Clock()

center = (320, 240)
radius = 200

def draw_clock_face():
    screen.fill((255, 255, 255)) 

#Tegmner cirkel til ur
    pygame.draw.circle(screen, (0, 0, 0), center, radius, 2)

#Hver 30 grad = 1 time
    for angle in range(0, 360, 30):  
        x_outer = center[0] + radius * math.cos(math.radians(angle))
        y_outer = center[1] + radius * math.sin(math.radians(angle))
        x_inner = center[0] + (radius - 20) * math.cos(math.radians(angle))
        y_inner = center[1] + (radius - 20) * math.sin(math.radians(angle))
        pygame.draw.line(screen, (0, 0, 0), (x_inner, y_inner), (x_outer, y_outer), 3) #Timeviser

def draw_hand(angle_deg, length, color, width):
    angle_rad = math.radians(angle_deg - 90)  # -90 for at starte kl. 12 (0 grad python - til højre)
    end_x = center[0] + length * math.cos(angle_rad)
    end_y = center[1] + length * math.sin(angle_rad)
    pygame.draw.line(screen, color, center, (end_x, end_y), width)

#Lykke (bliver ved til vinduet lukkes)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#Baggrund + tVisere
    draw_clock_face()

    now = datetime.datetime.now()
    second = now.second
    minute = now.minute
    hour = now.hour % 12

    second_angle = second * 6                   
    minute_angle = minute * 6 + second * 0.1    
    hour_angle = hour * 30 + minute * 0.5       

    draw_hand(hour_angle, 80, (0, 0, 0), 8)
    draw_hand(minute_angle, 120, (0, 0, 0), 6)
    draw_hand(second_angle, 150, (255, 0, 0), 2)

    pygame.display.flip()
    clock.tick(60)