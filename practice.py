import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
#surface = pygame.Surface((100, 100))
done = False
screen.fill((255, 255, 255))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    #surface = pygame.Surface((50, 50))
    surface = pygame.Surface((100, 100))
    surface.fill((255, 255, 255))

    pygame.draw.circle(surface, (0,0,0), (25,25),25)
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    screen.blit(surface, (20,10))

    pygame.display.flip()