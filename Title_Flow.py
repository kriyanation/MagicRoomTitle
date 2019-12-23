import pygame
import sqlite3
import Data_Flow
import pyttsx3


WINDOW_WIDTH = 1900
WINDOW_HEIGHT = 1000

CLASS_CONTEXT_WIDTH = 500
CLASS_CONTEXT_HEIGHT = 1000
d_text = ''
forward_count = 0
backward_count = 0

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
text_font = pygame.font.Font("Quite Magical - TTF.ttf", 42)
title_font = pygame.font.Font("Quite Magical - TTF.ttf", 48)
list_names = []
title_text = Data_Flow.get_Title()

def type_writer(t_surface, display_text,start_pos,text_font, rgb):
    global WINDOW_HEIGHT, WINDOW_WIDTH, d_text
    list_text = list(display_text)
    for element in list_text:
        d_text += element
        text_surface = text_font.render(element, True, rgb)
        x, y = start_pos
        start_pos = x+15, y
        t_surface.blit(text_surface, start_pos)
        pygame.display.update()
        pygame.time.wait(60)
    engine.setProperty('voice', 'english+m2')
    engine.setProperty('rate', 150)
    engine.say(quote)
    engine.runAndWait()

def text_render(t_surface, text,pos,rgb):
    text_surface = title_font.render(text, True, rgb)
    t_surface.blit(text_surface,pos)

def voice_title(text):
    engine.setProperty('voice', 'english+f3')
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()







connection = sqlite3.connect("/home/ram/MagicRoom.db")
cur = connection.cursor()
sql = "select * from Magic_Class_Info"
cur.execute(sql)
rows = cur.fetchall()
for element in rows:
    list_names.append(element)
connection.commit()
connection.close()


quote = Data_Flow.get_Quote()
quote_text = text_font.render(quote, True, (255,255,200))

engine = pyttsx3.init(driverName='espeak')


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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            forward_count += 1
            if forward_count == 1:
                voice_title(title_text)


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


    if len(d_text) == 0:
        type_writer(title_surface, quote, (150, 50), text_font, (255, 255, 200))
    else:
        title_surface.blit(quote_text, (150, 50))
    text_render(title_surface, title_text, (800, 100), (25, 255, 50))
    title_surface.blit(class_context_surface, (1400, 5))

    pygame.display.flip()



