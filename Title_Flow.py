import pygame
import sqlite3





WINDOW_WIDTH = 1900
WINDOW_HEIGHT = 1000
FPS = 10
pygame.init()
title_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Magic Room")
background = pygame.image.load('background_CR.jpg').convert()
medal = pygame.image.load('medal.png').convert()
premium = pygame.image.load('premium-badge.png').convert()
class_font = pygame.font.Font("Quite Magical - TTF.ttf", 42)
header_surface_name = class_font.render("Name", True,(0, 255, 0))
header_surface_badge = class_font.render("Badge", True,(0, 255, 0))
header_surface_points = class_font.render("Points", True,(0, 255, 0))
data_font = pygame.font.Font("Quite Magical - TTF.ttf", 26)
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


while True:
    fpsclock.tick(FPS)
    for event in pygame.event.get():  # event handling loop
        if event.type == pygame.QUIT:
            exit()
    title_surface.blit(background, (0,0))
    pygame.draw.rect(title_surface,(0,255,0),pygame.Rect((1400,0),(900,1000)),5)
    title_surface.blit(header_surface_name, (1420, 10))
    title_surface.blit(header_surface_badge, (1580, 10))
    title_surface.blit(header_surface_points, (1750, 10))
    draw_index = 0
    for element in list_names:
        name = data_font.render(element[0], True, (255, 255, 204))
        points = data_font.render(str(element[2]), True, (255, 255, 204))
        y = draw_index + 50
        title_surface.blit(name, (1420, y))
        if element[1] == 'm':
            title_surface.blit(medal, (1600, y))
        else:
            title_surface.blit(premium, (1600, y))
        title_surface.blit(points, (1770, y))
        draw_index += 30
    pygame.display.update()



