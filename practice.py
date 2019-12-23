import pygame
import pyttsx3

pygame.init()
screen = pygame.display.set_mode((400, 300))
#surface = pygame.Surface((100, 100))
done = False
screen.fill((255, 255, 255))


engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
engine.setProperty('voice', 'en-westindies+m6')
engine.setProperty('gender','female')
engine.setProperty('rate', 120)
engine.say("We are all in the same boat")
engine.runAndWait()
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