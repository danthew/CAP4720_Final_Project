# PyGame template.
 
# Import standard modules.
import sys
 
# Import non-standard modules.
import pygame
from pygame.locals import *

black = (0, 0, 0)
white = (255, 255, 255)

width, height = 1200, 900

#pygame.init()
 
class Title:

    def draw(self, screen):
        screen.fill((255, 165, 0)) # Fill the screen with black.

        # Redraw screen here.
        smallfont = pygame.font.SysFont('Arial', 50)
        bigfont = pygame.font.SysFont('Arial', 100)

        # For title screen
        # Game title
        title = bigfont.render('Speed Demon', True, (255, 255,255))
        screen.blit(title, (width/2 - 320, 100))
        
        # Play button
        play_rect = pygame.Rect(0, 0, 280, 80)
        play_rect.center = (width/2, height/2)
        pygame.draw.rect(screen, (105, 105, 105), play_rect)
        play = smallfont.render('PLAY', True, (255, 255, 255))
        text_rect = play.get_rect(center=(width/2, height/2))
        screen.blit(play, text_rect)

        # Exit button
        exit_rect = pygame.Rect(0, 0, 280, 80)
        exit_rect.center = (width/2, height/2 + 110)
        pygame.draw.rect(screen, (105, 105, 105), exit_rect)
        exit = smallfont.render('EXIT', True, (255, 255,255))
        text_rect2 = exit.get_rect(center=(width/2, height/2 + 110))
        screen.blit(exit, text_rect2)

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
                        if height/2 - 40 <= mouse[1] <= height/2 + 40:
                            titleActive = False
                            # Change to main gameplay
                        elif height/2 + 70 <= mouse[1] <= height/2 + 150:
                            pygame.quit()
                            sys.exit()