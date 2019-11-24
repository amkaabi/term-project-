import pygame



import random 



pygame.init()


pygame.font.init()
############  pics ######################
#https://freeartbackgrounds.com/?1318,sand-from-desert-background
#sand background
backPicDes="sand.png"
#https://www.chupamobile.com/ui-graphic-asset/3
#-set-nature-and-desert-game-background-14764
#mainpage link
mainPg='mainPg.png'
goastLeft=10*['gleft1.png','gleft2.png','gleft3.png','gleft4.png']
goastRight=10*['gright1.png','gright2.png','gright3.png','gright4.png']
#https://ya-webdesign.com/download.html scorpion right and left
scorpionLeft=10*['sleft1.png','sleft2.png','sleft3.png',
'sleft4.png','sleft5.png','sleft6.png']
scorpionRight=10*['sright1.png','sright2.png','sright3.png',
'sright4.png','sright5.png','sright6.png']
#charectar with dof link https://ya-webdesign.com/download.html
dogRight=5*['doRight.png']
dogLeft=5*['doLeft.png']
#burger link
#https://www.foxnews.com/food-drink/we-tried-ihops-new-pancake-burger
ch1Pic='BURGER.png'
ch2Pic=ch1Pic
################## fonts ################
################## Varibales ############
#each enemy have different (vel,x,y,start,end,width) variables
#g(goast), s(scprpion), d(dog with the monster)
#each player has different(x,y,start,end,width) Vel stand for step
vel=50
step=50
wndW=551
wndH=751
chX1=wndW/2+vel//2
chY1=wndH-vel
chY2=chY1
chX2=chX1+vel
sVel=5
sEnd=wndW
sStart=0
sX=sStart
sY=step
sW=42
gVel=5
gEnd=sEnd
gStart=0
gX=gStart
gY=4*step
gW=33
dStart=100
dEnd=wndW-100
dVel=20
dX=dStart
dY=7*step
dw=45
dH=45
gH=45
sH=45
sX2=0
sY2=9*step
sVel2=17
sStart2=0
sEnd2=wndW
gX2=75
gStart2=75
gEnd2=wndW
gY2=11*step
gVel2=12
dStart2=0
dEnd2=wndW-200
dVel2=14
dX2=0
dY2=3*step
#the popup text x and y 
textX=wndW-100
textY=wndH-30
#########################################
#the caption and screen created
pygame.display.set_caption("CROSSIN'")
screen=pygame.display.set_mode((wndW,wndH))
#font and messages created and assigned  
font = pygame.font.Font('freesansbold.ttf', 30)
gO=font.render('GAME OVER', True,[255,0,0])
w1=font.render('PLAYER1 WON close screen to exit', True,[0,255,0])
w2=font.render('PLAYER2 WON close screen to exit', True,[0,255,0])
#the while loops main varbles created
gameOver=True
clScreen=False
clock=pygame.time.Clock()
#the class to create background 
class background:
    def __init__(self,backPic):
        self.backPic=pygame.image.load(backPic).convert()
#the class to create charcters 
class player:
    def __init__(self,chX,chY,vel,chPic):
        self.chX=chX
        self.chY=chY
        self.chPic=chPic
        self.vel=vel
        self.box=(self.chX,self.chY,50,45)
    def draw(self,screen):
        self.chLoad=pygame.image.load(self.chPic).convert_alpha(screen)
        screen.blit(self.chLoad,[self.chX,self.chY])
        self.box=(self.chX,self.chY,50,45)
        #pygame.draw.rect(screen,[0,0,255],self.box,2)
    def hit(self):
        return True
#the class to create enemies
class enemy:
    def __init__(self,rightPics,leftPics,y,x,vel,start,end,screen,w,boxH):
        self.x=x
        self.w=w
        self.y=y
        self.boxH=boxH
        self.vel=vel
        self.end=end
        self.start=start
        self.rightPics=rightPics
        self.leftPics=leftPics
        self.end=end
        self.xCount=0
        self.steps=0
        self.ratio=0
        self.box=(self.x,self.y,self.w,self.boxH)
#the function will take care of movment
    def movment(self):
        if self.xCount+1>=self.steps:
            self.xCount=0
        if self.vel>0:
            if self.x+self.vel+self.w<self.end:
                self.x=self.x+self.vel
                self.xCount+=1
            else:
                self.vel=self.vel*-1
                self.xCount=0
        elif self.vel<0:
            if self.x>self.start:
                self.x=self.x+self.vel
                self.xCount+=1
            else:
                self.vel=self.vel*-1
                self.xCount=0
#the function would create the pictures change
    def pics(self,screen):
        self.movment()
        self.steps=(self.end-self.start)//self.vel
        self.ratio=round(self.steps/len(self.rightPics))
        self.curX=(self.xCount//self.ratio)
        if self.vel>0:
            self.picR=pygame.image.load(self.rightPics[self.curX-1]).convert_alpha(screen)
            screen.blit(self.picR,[self.x,self.y])
        if self.vel<=0:
            self.picL=pygame.image.load(self.leftPics[self.curX-1]).convert_alpha(screen)
            screen.blit(self.picL,[self.x,self.y])
        self.box=(self.x,self.y,self.w,45)
        #pygame.draw.rect(screen,[0,0,255],self.box,2)

#the enemies and players are created bellow
mp=background(mainPg)
burger=player(chX1,chY1,vel,ch1Pic)
desert=background(backPicDes)
dog=enemy(dogRight,dogLeft,dY,dX,dVel,dStart,dEnd,screen,dw,dH)
scorpion1=enemy(scorpionRight,scorpionLeft,sY,sX,sVel,sStart,sEnd,screen,sW,sH)
goast1=enemy(goastRight,goastLeft,gY,gX,gVel,gStart,gEnd,screen,gW,gH)
burger2=player(chX2,chY2,vel,ch2Pic)
s1=scorpion1
g1=goast1
g2=enemy(goastRight,goastLeft,gY2,gX2,gVel2,gStart2,gEnd2,screen,gW,gH)
s2=enemy(scorpionRight,scorpionLeft,sY2,sX2,sVel2,sStart2,sEnd2,screen,sW,sH)
d2=enemy(dogRight,dogLeft,dY2,dX2,dVel2,dStart2,dEnd2,screen,dw,dH)
#this function would make the chrecters move
def movment(event,charecter1,vel,wndW,Player,wndH):
#the movment for the first player
    if Player==1:
         if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and charecter1.chX>vel:
                 charecter1.chX=charecter1.chX-vel
            if event.key==pygame.K_RIGHT and wndW-(2*vel)>charecter1.chX:
                charecter1.chX=charecter1.chX+vel
            if event.key==pygame.K_UP and vel<charecter1.chY:
                charecter1.chY=charecter1.chY-vel
            if event.key==pygame.K_DOWN and wndH-(vel)>charecter1.chY:
                charecter1.chY=charecter1.chY+vel
#the movment for the secound player
    if Player==2:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a and charecter1.chX>vel:
                    charecter1.chX=charecter1.chX-vel
                if event.key==pygame.K_d and wndW-(2*vel)>charecter1.chX:
                    charecter1.chX=charecter1.chX+vel
                if event.key==pygame.K_w and vel<charecter1.chY:
                    charecter1.chY=charecter1.chY-vel
                if event.key==pygame.K_s and wndH-(vel)>charecter1.chY:
                    charecter1.chY=charecter1.chY+vel
#this function would show the main page(instructions page)
def mainPg(clScreen,mainPage,screen):
    while not clScreen:
        screen.blit(mainPage.backPic,[0,0])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    key='One'
                    clScreen=True
                if event.key==pygame.K_t:
                    key='Two'
                    clScreen=True
        pygame.display.update()
    return key
#this functions will draw all of chaterters and enemies on the game screen
def drawDesert(screen,count):
    screen.blit(desert.backPic,[0,0])
    scorpion1.pics(screen)
    burger.draw(screen)
    dog.pics(screen)
    goast1.pics(screen)
    d2.pics(screen)
    s2.pics(screen)
    g2.pics(screen)
    if count==2:
        burger2.draw(screen)
#the clash function will detect the clashes between chaterters and enemies
def clash(e,p,pt,count,go):
    if count==1:
#if one player clash enemy return game Over screen
        if p.box[1]<e.box[1]+e.box[3] and p.box[1]+p.box[3]>e.box[1]:
            if p.box[0]+p.box[2]>e.box[0] and p.box[0]<e.box[0]+e.box[2]:
                if p.hit()== True:
                    screen.fill([255,255,255])
                    screen.blit(gO,(0,350))
                    pygame.display.update()
                    pygame.time.wait(200)
                    return True
#if one of the two chaterters clash with enemy then the chaterter restart 
    if count!=1:
        if p.box[1]<e.box[1]+e.box[3] and p.box[1]+p.box[3]>e.box[1]:
            if p.box[0]+p.box[2]>e.box[0] and p.box[0]<e.box[0]+e.box[2]:
                if p.hit()== True:
                    p.chY=chY1
                    p.chX=chX1
        if pt.box[1]<e.box[1]+e.box[3] and pt.box[1]+pt.box[3]>e.box[1]:
            if pt.box[0]+pt.box[2]>e.box[0] and pt.box[0]<e.box[0]+e.box[2]:
                if pt.hit()== True:
                    pt.chY=chY2
                    pt.chX=chX2
                    
#this function would detect the clashes and return True
def enemies(e1,e2,e3,e4,e5,e6,gO,count,ch2,ch1):
    if clash(e1,ch1,ch2,count,gO)==True:
        return True
    if clash(e2,ch1,ch2,count,gO)==True:
        return True
    if clash(e3,ch1,ch2,count,gO)==True:
        return True
    if clash(e4,ch1,ch2,count,gO)==True:
        return True
    if clash(e5,ch1,ch2,count,gO)==True:
        return True
    if clash(e6,ch1,ch2,count,gO)==True:
        return True
def g1Loop(ch1,ch2,e1,e2,e3,e4,e5,e6,mp,screen,gaOver,wndW,vel,wndH,gO,w2,w1):
#reset the first chaterter posion 
    ch1.chY=chY1
    ch1.chX=chX1
    clScreen=False
#this two if condtions would check the number of players and adjst count
    if'Two'in mainPg(clScreen,mp,screen):
        gameOver=False
        count=2
        ch2.chY=chY2
        ch2.chX=chX2
    if'One'in mainPg(clScreen,mp,screen):
        gameOver=False
        count=1

    while not gameOver:
#this functions would draw the charecters
        drawDesert(screen,count)
#this two if coundtions would check if one of the players won
#and the winning player will apper in the screen
        if ch2.chY<50:
            screen.fill([255,255,255])
            screen.blit(w2,(0,350))
            pygame.display.update()
            pygame.time.wait(200)
            gameOver=True
        if ch1.chY<50:
            screen.fill([255,255,255])
            screen.blit(w1,(0,350))
            pygame.display.update()
            pygame.time.wait(200)
            gameOver=True
#if the one charters crash with enemy gameOver will be False
        gameOver=enemies(e1,e2,e3,e4,e5,e6,gO,count,ch2,ch1)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameOver=True
            if count==1:
                movment(event,ch1,vel,wndW,1,wndH)
            else:
                movment(event,ch1,vel,wndW,1,wndH)
                movment(event,ch2,vel,wndW,2,wndH)
        pygame.display.flip()
        pygame.display.update()
#if the game ended the function would be recresivlly called to main page
    if gameOver==True:
        g1Loop(ch1,ch2,e1,e2,e3,e4,e5,e6,mp,screen,gameOver,wndW,vel,wndH,gO,w2,w1)
        
g1Loop(burger,burger2,g1,s1,dog,g2,s2,d2,mp,screen,gameOver,wndW,vel,wndH,gO,w2,w1)   
