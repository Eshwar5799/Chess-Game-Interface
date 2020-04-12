import pygame
import sys 
import time
pygame.init()

WIDTH_OF_SCREEN=1000
HEIGHT_OF_SCREEN=2000

Display=pygame.display.set_mode((WIDTH_OF_SCREEN,HEIGHT_OF_SCREEN))
pygame.display.set_caption("A Chess Game")

gray=(123, 131, 173)
white=(255,255,255)
gray=(128,130,128)
black=(0,0,0)
button_color=(100,100,100)




font_style = pygame.font.SysFont("bahnschrift", 25)
Display_font = pygame.font.SysFont("comicsansms", 35)
 

def gameloop():


    game_over=False
    
    
    while not game_over:
        for event in pygame.event.get():
           
            Display.fill(gray)
            b.DrawBoard()
            
            

            if(event.type==pygame.QUIT):
                game_over=True


        
        pygame.display.update()
    pygame.quit()
    quit()




class Board:
 
    ROWS=9
    COLS=9
    WIDTH=20
    HEIGHT=20
    MARGIN=5
    SIZE_OF_BLOCK=20
    
    def __init__(self,WIDTH=50,HEIGHT=50,ROWS=9,COLS=9,MARGIN=15,SIZE_OF_BLOCK=45):
        self.ROWS=ROWS
        self.COLS=COLS
        self.WIDTH=WIDTH
        self.HEIGHT=HEIGHT
        self.MARGIN=MARGIN
        self.SIZE_OF_BLOCK=SIZE_OF_BLOCK
        
    def DrawBoard(self):
        
        height=self.HEIGHT
        width=self.WIDTH
        size_of_block=self.SIZE_OF_BLOCK
        margin=self.MARGIN
        cnt=0
        for i in range(1,self.ROWS+1):
            
            for j in range(1,self.COLS+1):
                if cnt%2==0:
                    pygame.draw.rect(Display,white,[(margin+width)*i,(margin+height)*j,size_of_block,size_of_block])
                else:
                    pygame.draw.rect(Display,black,[(margin+width)*i,(margin+height)*j,size_of_block,size_of_block])
                
                cnt+=1    

        pygame.draw.aaline(Display,white,(700,0),(700,2000))

      
        

    

        






            

                

        

if __name__ == "__main__":
    b=Board()
    gameloop()




