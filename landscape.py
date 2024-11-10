import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

sky_color = [135, 206, 250]
grass_color = (34, 139, 34)
sun_color = (255, 223, 0)
cloud_color = (255, 255, 255)
house_color = (139, 69, 19)
roof_color = (165, 42, 42)

sun_radius = 50
sun_max_radius = 70
sun_min_radius = 50
sun_growing = True

cloud_pos = [-100, 100]
cloud_speed = 2

house_pos = [300, 350]

frame_count = 0

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(sky_color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, grass_color, pygame.Rect(0, height // 2, width, height // 2))
  
    pygame.draw.circle(screen, sun_color, (width - 100, 100), int(sun_radius))

    pygame.draw.rect(screen, house_color, pygame.Rect(house_pos[0], house_pos[1], 100, 100))
    pygame.draw.polygon(screen, roof_color, [(house_pos[0] - 10, house_pos[1]), 
                                             (house_pos[0] + 50, house_pos[1] - 50), 
                                             (house_pos[0] + 110, house_pos[1])])

    pygame.draw.ellipse(screen, cloud_color, pygame.Rect(cloud_pos[0], cloud_pos[1], 80, 40))
    pygame.draw.ellipse(screen, cloud_color, pygame.Rect(cloud_pos[0] + 30, cloud_pos[1] - 10, 70, 50))
    pygame.draw.ellipse(screen, cloud_color, pygame.Rect(cloud_pos[0] + 60, cloud_pos[1], 80, 40))

    cloud_pos[0] += cloud_speed
    if cloud_pos[0] > width:
        cloud_pos[0] = -150
        cloud_pos[1] += 10
    if cloud_pos[1] >= 220:
        cloud_pos[1] = 100  

    frame_count += 1
    if frame_count % 200 == 0:
        if sky_color[1] > 100:
            sky_color[1] -= 10
        elif sky_color[1] <= 100:
            sky_color = [135, 206, 250]

    if sun_growing:
        sun_radius += 0.2
        if sun_radius >= sun_max_radius:
            sun_growing = False
    else:
        sun_radius -= 0.2
        if sun_radius <= sun_min_radius:
            sun_growing = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
