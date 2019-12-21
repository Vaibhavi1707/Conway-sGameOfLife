import pygame
from math import*
from finalgol import*
pygame.init()
display_width=1200
display_height=1000
red=(200,0,0)
bright_red=(255,0,0)
white=(255,255,255)
yellow=(200,200,0)
bright_yellow=(255,255,0)
black=(0,0,0)
green=(0,200,0)
bright_green=(0,255,0)
blue=(0,0,200)
greenblue=(0,200,255)
bright_blue=(0,0,255)
x=display_width*0.2
y=display_height*0.1
continue_buttonx=150
continue_buttony=850
continue_button_width=170
continue_button_height=50
changetheme_buttonx=1000
reset_buttonx=500
changetheme_buttony=100
changetheme_button_width=170
changetheme_button_height=50
quit_buttonx=850
inst_buttonx=450
quit_buttony=850
quit_button_width=100
quit_button_height=50
reset=0
gameDisplay=pygame.display.set_mode((display_width,display_height))
introgameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("The Conway's Game Of Life")
clock=pygame.time.Clock()
block_width=73
continue_play=False
grid_array=[[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]
def Instructions():
    instruct=True
    while instruct:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                instruct=False 
                pygame.quit()
                quit()
        gameDisplay.fill(bright_red)
        message_display("The Conway's Game Of Life",50,170,20,800,70,bright_yellow)
        InstImg=pygame.image.load("instruction.jpg").convert()
        gameDisplay.blit(InstImg,(100,100))
        button(continue_buttonx,continue_buttony,continue_button_width,continue_button_height,bright_green,green,"play",20,"PLAY")
        button(quit_buttonx,quit_buttony,quit_button_width,quit_button_height,bright_blue,blue,"quit",20,"QUIT")
        pygame.display.update()
        clock.tick(15)
def display_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid_array[i][j]==1:
               pygame.draw.rect(gameDisplay,white,(x+j*block_width,y+i*block_width,block_width,block_width))
def grid(x,y):
    for i in range(0,9):
        for j in range(0,9):
            pygame.draw.rect(gameDisplay,black,(x+i*73,y+j*73,73,73))
    for i in range(10):
        pygame.draw.line(gameDisplay,white,(x+i*73,y),(x+i*73,y+9*73))
    for p in range(10):
        pygame.draw.line(gameDisplay,white,(x,y+p*73),(x+9*73,y+p*73))
def text_objects(text,font,color):
    Text_surface=font.render(text,True,color)
    return Text_surface,Text_surface.get_rect()
def message_display(text,size,x,y,w,h,c):
    smallText=pygame.font.Font("freesansbold.ttf",size)
    TextSurf,TextRect=text_objects(text,smallText,c)
    TextRect.center=(x+(w/2),y+(h/2))
    gameDisplay.blit(TextSurf,TextRect)
def hover_and_functionality(x,y,w,h,c1,c2,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    t=0
    if x<mouse[0]<x+w and y<mouse[1]<y+h:
       pygame.draw.rect(gameDisplay,c1,(x,y,w,h))
       if click[0]==1 and action!=None:
           if action=="play":
              continue_play=True
              gameloop()
           elif action=="quit":
              pygame.quit()
              quit()
           elif action=="continue":
              finalgrid=main(grid_array)
              display_grid(finalgrid)
           elif action=="reset":  
              for i in range(len(grid_array)):
                  for j in range(len(grid_array[0])):
                      if grid_array[i][j]==1:
                         grid_array[i][j]=0
              gameloop()
           elif action=="instructions":
              Instructions()
    else:
       pygame.draw.rect(gameDisplay,c2,(x,y,w,h))
def button(x,y,w,h,c1,c2,a,s,p):
    hover_and_functionality(x,y,w,h,c1,c2,a)
    message_display(p,s,x,y,w,h,black)
def gameloop():
    x_change=0
    x1=0
    y1=0
    crashed=False
    stop=False
    c2=white
    c1=black
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True
                pygame.quit()
                quit()
            gameDisplay.fill(bright_red)
            #grid(x,y,bgcol,col)
            #change=button(changetheme_buttonx,changetheme_buttony,changetheme_button_width,changetheme_button_height,bright_yellow,yellow,"change",20,"COLOUR MODE")
            button(reset_buttonx,continue_buttony,changetheme_button_width,changetheme_button_height,bright_yellow,yellow,"reset",20,"RESET")
            #grid(x,y,c1,c2)
            '''if change==1:
                c1=bright_green
                c2=bright_blue'''
            grid(x,y)
            message_display("The Conway's Game Of Life",50,170,20,800,70,bright_yellow)
            button(continue_buttonx,continue_buttony,continue_button_width,continue_button_height,bright_green,green,"continue",20,"GO!")
            button(quit_buttonx,quit_buttony,quit_button_width,quit_button_height,bright_blue,blue,"quit",20,"QUIT")
            mouse_x=pygame.mouse.get_pos()[0]
            mouse_y=pygame.mouse.get_pos()[1]
            if x<mouse_x<x+9*block_width and y<mouse_y<y+9*block_width:
               if event.type==pygame.MOUSEBUTTONDOWN:
                  grid_array[floor((mouse_y-y)/block_width)][floor((mouse_x-x)/block_width)]=1
            #print(grid_array)
        display_grid(grid_array)
        pygame.display.update()
        clock.tick(60)
def Game_Intro():
    #print("HI")
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                intro=False 
                pygame.quit()
                quit()
        bgImg=pygame.image.load("index.png").convert()
        gameDisplay.blit(bgImg,(0,0))
        message_display("Welcome To the Conway's Game Of Life",60,100,100,1000,500,white)
        button(continue_buttonx,500,continue_button_width,continue_button_height,bright_green,green,"play",20,"PLAY")
        button(quit_buttonx,500,quit_button_width,quit_button_height,bright_red,red,"quit",20,"QUIT")
        button(inst_buttonx,500,continue_button_width,continue_button_height,bright_yellow,yellow,"instructions",20,"INSTRUCTIONS")
        pygame.display.update()
        clock.tick(15)
          
if __name__=="__main__":
   Game_Intro()
   gameloop()
   pygame.quit()
   quit()
