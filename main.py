import pygame
import sys 
import time
import pygbutton
pygame.init()

WIDTH_OF_SCREEN=1000
HEIGHT_OF_SCREEN=2000

Display=pygame.display.set_mode((WIDTH_OF_SCREEN,HEIGHT_OF_SCREEN))
pygame.display.set_caption("A Chess Game")

gray=(123, 131, 173)
white=(255,255,255)
gray=(128,130,128)
black=(105,105,105)
button_color=(36,160,237)




font_style = pygame.font.SysFont("bahnschrift", 25)
Display_font = pygame.font.SysFont("comicsansms", 35)
 

def gameloop():


    game_over=False
    
    
    while not game_over:
        for event in pygame.event.get():
           
            Display.fill(gray)
            
            
            

            if(event.type==pygame.QUIT):
                game_over=True


        b.DrawBoard()
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

    
    def text_to_button(self,msg,color,buttonx,buttony,buttonwidth,buttonheight,size="small"):
        textSurf,textRect= self.text_objects(msg,color,size)
        textRect.center=((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
        Display.blit(textSurf,textRect)

    def text_objects(self,msg,color,size="small"):
        textSurface=Display_font.render(msg,True,color)
        return textSurface,textSurface.get_rect()

        
        
    def DrawBoard(self):
        
        height=self.HEIGHT
        width=self.WIDTH
        size_of_block=self.SIZE_OF_BLOCK
        margin=self.MARGIN
        cnt=0
        for i in range(1,self.ROWS):
            
            for j in range(1,self.COLS+1):
                if cnt%2==0:
                    pygame.draw.rect(Display,white,[(margin+width)*i,(margin+height)*j,size_of_block,size_of_block])
                else:
                    pygame.draw.rect(Display,black,[(margin+width)*i,(margin+height)*j,size_of_block,size_of_block])
                
                cnt+=1    

        pygame.draw.aaline(Display,white,(700,0),(700,2000))

        ''' Button '''

        Button_start=pygame.draw.rect(Display,white,(250,750,170,50))
        '''start button'''
        self.text_to_button("Start",button_color,250,750,170,50)

        ''' White players '''

        Images.loadImageWhite(self)

        ''' Black players '''
        Images.loadImageBlack(self)

        
        



class Images:
    def __init__(self):
        pass

   
    def loadImageWhite(self):
        ''' White on top side
            black on bottom side

            Difference of 60 is good
        '''
        Wrook=pygame.image.load("./Images/wrook.png")
        Display.blit(Wrook,(55,50))

        Wknight=pygame.image.load("./Images/wknight.png")
        Display.blit(Wknight,(115,50))

        Wbishop=pygame.image.load("./Images/wbishop.png")
        Display.blit(Wbishop,(180,50))

        Wqueen=pygame.image.load("./Images/wqueen.png")
        Display.blit(Wqueen,(250,50))

        Wking=pygame.image.load("./Images/wking.png")
        Display.blit(Wking,(320,50))

        Wbishop_2=pygame.image.load("./Images/wbishop.png")
        Display.blit(Wbishop_2,(380,50))

        Wknight_2=pygame.image.load("./Images/wknight.png")
        Display.blit(Wknight_2,(440,50))

        Wrook_2=pygame.image.load("./Images/wrook.png")
        Display.blit(Wrook_2,(510,50))

        '''Pawns'''
        PawnDistance=40
        for i in range(1,9):
            Wpawn=pygame.image.load("./Images/wpawn.png")
            Display.blit((Wpawn),( (24+PawnDistance)*i,120))

    def loadImageBlack(self):

        Brook=pygame.image.load("./Images/brook.png")
        Display.blit((Brook),(55,575))

        Bknight=pygame.image.load("./Images/bknight.png")
        Display.blit((Bknight),(120,575))

        Bbishop=pygame.image.load("./Images/bbishop.png")
        Display.blit((Bbishop),(180,575))

        Bqueen=pygame.image.load("./Images/bqueen.png")
        Display.blit((Bqueen),(250,575))

        Bking=pygame.image.load("./Images/bking.png")
        Display.blit((Bking),(310,575))

        Bbishop_2=pygame.image.load("./Images/bbishop.png")
        Display.blit((Bbishop),(380,575))

        Bknight_2=pygame.image.load("./Images/bknight.png")
        Display.blit((Bknight_2),(440,575))

        Brook_2=pygame.image.load("./Images/brook.png")
        Display.blit((Brook_2),(510,575))


        '''Black pawns'''
        PawnDistanceBlack=40
        for i in range(1,9):
            Bpawn=pygame.image.load("./Images/bpawn.png")
            Display.blit(Bpawn,((24+PawnDistanceBlack)*i,510))






        



        
        



    

      
        

    

        






            

                

        

if __name__ == "__main__":
    b=Board()
    gameloop()




