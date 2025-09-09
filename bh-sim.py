import pygame

pygame.init()

screen = pygame.display.set_mode(size=(500,500))
pygame.display.set_caption('Black Hole Simulation')
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False 


