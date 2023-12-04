import sys
import pygame
from pygame.locals import *

black = (0, 0, 0)
white = (255, 255, 255)

width, height = 1200, 900
 
class Title:

    def draw(self, screen):
        # Draw background image
        bg = pygame.image.load("./textures/bg.jpg").convert()
        screen.blit(bg, (0, -275))

        # Redraw screen here.
        smallfont = pygame.font.SysFont('Arial', 50)
        bigfont = pygame.font.SysFont('Arial', 100)

        # For title screen
        # Game title
        title = bigfont.render('Speed Demon', True, (255, 255, 255))
        text_rect = title.get_rect(center=(width/2, 150))
        screen.blit(title, text_rect)
        
        # Play button
        play_rect = pygame.Rect(0, 0, 280, 80)
        play_rect.center = (width/2, height/2 - 100)
        pygame.draw.rect(screen, (105, 105, 105), play_rect)
        play = smallfont.render('PLAY', True, (255, 255, 255))
        text_rect2 = play.get_rect(center=(width/2, height/2 - 100))
        screen.blit(play, text_rect2)

        # Exit button
        exit_rect = pygame.Rect(0, 0, 280, 80)
        exit_rect.center = (width/2, height/2 + 10)
        pygame.draw.rect(screen, (105, 105, 105), exit_rect)
        exit = smallfont.render('EXIT', True, (255, 255,255))
        text_rect3 = exit.get_rect(center=(width/2, height/2 + 10))
        screen.blit(exit, text_rect3)

        # Flip the display so that the things we drew actually show up.
        pygame.display.flip()
    
    def runPyGame(self):
        fps = 60.0
        fpsClock = pygame.time.Clock()
        screen = pygame.display.set_mode((width, height))
        titleActive = True

        dt = 1/fps
        while titleActive == True:
            self.draw(screen)
            dt = fpsClock.tick()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if width/2 - 140 <= mouse[0] <= width/2 + 140:
                        if height/2 - 140 <= mouse[1] <= height/2 - 60:
                            titleActive = False
                            # Change to main gameplay
                        elif height/2 - 30 <= mouse[1] <= height/2 + 50:
                            pygame.quit()
                            sys.exit()