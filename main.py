import pygame
import sys 
pygame.init()

WIDTH=1200
HEIGHT=800

Display=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("A Chess Game")

gray=(123, 131, 173)

def gameloop():


    game_over=False
    while not game_over:
        for event in pygame.event.get():
            Display.fill(gray)
            if(event.type==pygame.QUIT):
                game_over=True

        pygame.display.update()
    pygame.quit()
    quit()


if __name__ == "__main__":
    gameloop()




