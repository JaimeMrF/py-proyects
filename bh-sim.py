import pygame

pygame.init()

screen = pygame.display.set_mode(size=(500,500))
pygame.display.set_caption('Black Hole Simulation')
running = True

screen.fill(color="black")


black_hole = pygame.draw.circle(screen,'white', (screen.get_width()/2,screen.get_height()/2 ), 50, 1)
black_hole_ring = pygame.draw.ellipse(screen,'white', ((screen.get_width()/4),(screen.get_height()/2)-2, 250, 4), 1)
black_hole_rect = pygame.draw.rect(screen, 'white', ((screen.get_width()/2)-150, screen.get_height()/2-150, 300, 300), 1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False 
    pygame.display.update()


