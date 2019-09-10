import pygame
import time
import numpy as np

pygame.init()
gamewin = pygame.display.set_mode((650,400))
pygame.display.set_caption("flappy bird ")

bg = pygame.image.load("background-day.png")
pipes = pygame.image.load("pipe-green.png")
flipped_pipes = pygame.transform.flip(pipes,1,1)
play = [pygame.image.load("bird.png"),pygame.image.load("bird2.png"),pygame.image.load("bird3.png"),pygame.image.load("bird.png"),pygame.image.load("bird2.png"),pygame.image.load("bird3.png"),pygame.image.load("bird.png"),pygame.image.load("bird2.png"),pygame.image.load("bird3.png")]

pipe = False

def text_objects(text, font):
	textSurface = font.render(text, True,(0,0,0))
	return textSurface, textSurface.get_rect()
def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',70)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((700/2),(400/2))
	gamewin.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(2)
	


def seecollisions(x1,y1,w1,h1,x2,y2,w2,h2):
	if(x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
		return True
	elif(x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
		return True
	elif(x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
		return True
	elif(x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
		return True
	else:
		return False


class birdy(pygame.sprite.Sprite):
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.pipe = False
		self.jumpcount= 0
		self.space = False
		self.hitbox= (self.x,self.y,self.width,self.height)
		self.rect = pygame.Rect(self.hitbox)
		

	def draw(self,win,obj):
		if self.jumpcount+1 > 27:
			self.jumpcount =0
		if self.space:
			win.blit(obj[self.jumpcount//3],(self.x,self.y))
			

		else:
			win.blit(obj[0],(self.x,self.y))
		self.hitbox= (self.x,self.y,self.width,self.height)

		pygame.draw.rect(gamewin,(255,0,0),self.hitbox,2)
		self.rect = pygame.Rect(self.hitbox)
		


		self.jumpcount +=1



class piper(pygame.sprite.Sprite):
	def __init__(self,box_x,box_y,bxuppery,width,height):
		self.width = width
		self.height = height
		self.box_x =box_x
		self.box_y = box_y
		self.bxuppery = bxuppery
		self.hitbox= (self.box_x+20,self.box_y+20,64,64)
		self.rect = pygame.Rect(self.hitbox)
		self.hitboxup= (self.box_x,self.box_y-self.bxuppery,self.width,self.height-180)



	def draw(self,win,obj,fobj):
		win.blit(obj,(self.box_x,self.box_y))
		self.hitbox= (self.box_x,self.box_y,self.width,self.height)
		self.hitboxup= (self.box_x,self.box_y-self.bxuppery,self.width,self.height-180)


		pygame.draw.rect(gamewin,(255,0,0),self.hitbox,2)
		pygame.draw.rect(gamewin,(255,0,0),self.hitboxup,2)

		self.rect = pygame.Rect(self.hitbox)
		

		win.blit(fobj,(self.box_x,self.box_y-self.bxuppery))






def redrawgame():

	gamewin.blit(bg,(0,0))
	bird.draw(gamewin,play)
	if pipe:
 		pipspawn1.draw(gamewin,pipes,flipped_pipes)
 		pipspawn2.draw(gamewin,pipes,flipped_pipes)
 		pipspawn3.draw(gamewin,pipes,flipped_pipes)
 		pipspawn4.draw(gamewin,pipes,flipped_pipes)



 		
	pygame.display.update()


box_x = 660
box_x2 = box_x + 200
box_x3 = box_x2 + 200
box_x4 = box_x3 +200


rin = True 

box_y1 = np.random.randint(low=100,high=380)
box_y2 = np.random.randint(low=100,high=380)
box_y3 = np.random.randint(low=100,high=380)
box_y4 = np.random.randint(low=100,high=380)
pipspawn1=piper(box_x, box_y1,420,52,500)
pipspawn2=piper(box_x2, box_y2,420,52,500)
pipspawn3=piper(box_x3, box_y3,420,52,500)
pipspawn4=piper(box_x4, box_y4,420,52,500)

bird = birdy(20,200,34,26)

gravity= 1
score= 0
collidedpipe = False

while rin:
	pygame.time.delay(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE] :
		if collidedpipe == False:
			bird.y-= 20
			bird.space = True
			gravity = 1

	if bird.x < 220:
		bird.x+=2
	if collidedpipe == False:
		bird.y+=5 * gravity
		gravity+= 0.2

	if bird.y > 380:
		pygame.quit()
		quit()

	if bird.x > 120:
		pipe = True
		if collidedpipe == False:
			pipspawn1.box_x -= 5
			pipspawn2.box_x -= 5
			pipspawn3.box_x -= 5
			pipspawn4.box_x -= 5

	if pipspawn1.box_x <- 80:	
		pipspawn1.box_x= 680
		pipspawn1.box_y =  np.random.randint(low=100,high=380)
		score+=1
		
	if pipspawn2.box_x <- 80:	
		pipspawn2.box_x= 680
		pipspawn2.box_y =  np.random.randint(low=100,high=380)
		score+=1

	if pipspawn3.box_x <- 80:	
		pipspawn3.box_x= 680
		pipspawn3.box_y =  np.random.randint(low=100,high=380)
		score+=1

	if pipspawn4.box_x <- 80:	
		pipspawn4.box_x= 680
		pipspawn4.box_y =  np.random.randint(low=100,high=380)
		score+=1

	# if score>1:
	# 	print("score is",score+1)
	#print(bird.hitbox[0],bird.hitbox[1],bird.hitbox[2],bird.hitbox[3])
	#print(pipspawn1.hitboxup[0],pipspawn1.hitboxup[1],pipspawn1.hitboxup[2],pipspawn1.hitboxup[3])
	collision1 = seecollisions(bird.hitbox[0],bird.hitbox[1],bird.hitbox[2],bird.hitbox[3],pipspawn1.hitboxup[0],pipspawn1.hitboxup[1],pipspawn1.hitboxup[2],pipspawn1.hitboxup[3])
	collision2 = seecollisions(bird.hitbox[0],bird.hitbox[1],bird.hitbox[2],bird.hitbox[3],pipspawn2.hitboxup[0],pipspawn2.hitboxup[1],pipspawn2.hitboxup[2],pipspawn2.hitboxup[3])
	collision3 = seecollisions(bird.hitbox[0],bird.hitbox[1],bird.hitbox[2],bird.hitbox[3],pipspawn3.hitboxup[0],pipspawn3.hitboxup[1],pipspawn3.hitboxup[2],pipspawn3.hitboxup[3])
	collision4 = seecollisions(bird.hitbox[0],bird.hitbox[1],bird.hitbox[2],bird.hitbox[3],pipspawn4.hitboxup[0],pipspawn4.hitboxup[1],pipspawn4.hitboxup[2],pipspawn4.hitboxup[3])
	#print(collision1,collision2,collision3,collision4)
	if(collision2 or collision1 or collision3 or collision4):
		collidedpipe= True
	if(pygame.sprite.collide_rect(bird,pipspawn1)):
		collidedpipe = True
	if(pygame.sprite.collide_rect(bird,pipspawn2)):
		collidedpipe = True
	if(pygame.sprite.collide_rect(bird,pipspawn3)):
		collidedpipe = True
	if(pygame.sprite.collide_rect(bird,pipspawn4)):
		collidedpipe = True
	if collidedpipe:
		message_display("game over")
		pipspawn1=piper(box_x, box_y1,420,52,500)
		pipspawn2=piper(box_x2, box_y2,420,52,500)
		pipspawn3=piper(box_x3, box_y3,420,52,500)
		pipspawn4=piper(box_x4, box_y4,420,52,500)

		bird = birdy(20,200,34,26)
		collidedpipe = False

		
	redrawgame()

pygame.quit()