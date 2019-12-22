import pygame
import sqlite3





WINDOW_WIDTH = 1900
WINDOW_HEIGHT = 1000

CLASS_CONTEXT_WIDTH = 500
CLASS_CONTEXT_HEIGHT = 1000

FPS = 10
pygame.init()
title_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),pygame.RESIZABLE)
class_context_surface = pygame.Surface((CLASS_CONTEXT_WIDTH, CLASS_CONTEXT_HEIGHT))
pygame.display.set_caption("Magic Room")
background = pygame.image.load('background_CR.jpg').convert()
background_points = pygame.image.load('sidepane.png').convert()
medal = pygame.image.load('medal.png').convert()
premium = pygame.image.load('premium-badge.png').convert()
class_font = pygame.font.Font("Quite Magical - TTF.ttf", 42)
header_surface_name = class_font.render("Name", True,(0, 255, 0))
header_surface_badge = class_font.render("Badge", True,(0, 255, 0))
header_surface_points = class_font.render("Points", True,(0, 255, 0))
data_font = pygame.font.Font("Quite Magical - TTF.ttf", 32)
list_names = []



connection = sqlite3.connect("/home/ram/MagicRoom.db")
cur = connection.cursor()
sql = "select * from Magic_Class_Info"
cur.execute(sql)
rows = cur.fetchall()
for element in rows:
    list_names.append(element)
connection.commit()
connection.close()




fpsclock = pygame.time.Clock()

class_context_surface.set_alpha(0)
while True:
    fpsclock.tick(FPS)

    for event in pygame.event.get():  # event handling loop
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                class_context_surface.set_alpha(255)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                class_context_surface.set_alpha(0)
    title_surface.blit(background, (0,0))
    class_context_surface.blit(background_points, (0,0))

   # pygame.draw.rect(title_surface,(0,255,0),pygame.Rect((1400,0),(900,1000)),5)
    class_context_surface.blit(header_surface_name, (5, 10))
    class_context_surface.blit(header_surface_badge, (170, 10))
    class_context_surface.blit(header_surface_points, (350, 10))
    draw_index = 0
    for element in list_names:
        name = data_font.render(element[0], True, (255, 255, 255))
        points = data_font.render(str(element[2]), True, (255, 255, 255))
        y = draw_index + 50
        class_context_surface.blit(name, (9, y))
        if element[1] == 'm':
            class_context_surface.blit(medal, (185, y))
        else:
            class_context_surface.blit(premium, (185, y))
        class_context_surface.blit(points, (365, y))
        draw_index += 30
    title_surface.blit(class_context_surface, (1400, 5))
    pygame.display.flip()



