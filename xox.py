import os
import sys, pygame

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

p1 = pygame.image.load("images/pl1.jpg")
p2 = pygame.image.load("images/pl2.jpg")
bg = pygame.image.load("images/bg.jpg")
fin = pygame.image.load("images/fin.jpg")
blank = pygame.image.load("images/blank.jpg")


# for old version doesn't need to be here
def printMap(map):

	print(' * ----- * ----- * ----- * ')

	print(" |       |       |       |\n |   {}   |   {}   |   {}   |\n |       |       |       |".format(map[0][0],map[0][1],map[0][2]))
	
	print(' * ----- * ----- * ----- * ')

	print(" |       |       |       |\n |   {}   |   {}   |   {}   |\n |       |       |       |".format(map[1][0],map[1][1],map[1][2]))
	
	print(' * ----- * ----- * ----- * ')

	print(" |       |       |       |\n |   {}   |   {}   |   {}   |\n |       |       |       |".format(map[2][0],map[2][1],map[2][2]))
	
	print(' * ----- * ----- * ----- * ')


def checkWin(map):
	for i in range(3):
		if map[i][0] == map[i][1] and map[i][0] == map[i][2]:
			if map[i][0]=='X':
				return 1
			elif map[i][0]=='O':
				return 2

	for i in range(3):
		if map[0][i] == map[1][i] and map[1][i] == map[2][i]:
			if map[0][i]=='X':
				return 1
			elif map[0][i]=='O':
				return 2

	if map[0][0] == map[1][1] and map[2][2] == map[1][1]:
		if map[0][0]=='X':
				return 1
		elif map[0][0]=='O':
			return 2

	if map[0][2] == map[1][1] and map[2][0] == map[1][1]:
		if map[1][1]=='X':
				return 1
		elif map[1][1]=='O':
			return 2

	return 0


def redrawGameWindow(map):
	move = ['0','0','0','0','0','0','0','0','0']

	k=0
	for i in map:
		for j in i:
			if j=='X':
				move[k]='1'
				k+=1
			elif j=='O':
				move[k]='2'
				k+=1
			else:
				move[k]='0'
				k+=1
	screen.blit(bg, (0,0))
	k=0
	for i in range(35,376,170):
		for j in range(35,376,170):
			if move[k]=='1':
				screen.blit(p1, (i,j))
			elif move[k]=='2':
				screen.blit(p2, (i,j))
			k+=1
	

	pygame.display.update()




map = [	['1','2','3'],
		['4','5','6'],
		['7','8','9'],]
round = True
box = 0
win = 0
pos = 0
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.MOUSEBUTTONUP: pos = pygame.mouse.get_pos()

	
	if checkWin(map)!=0:
		if checkWin(map)==1:
			screen.blit(fin,(0,0))
			screen.blit(p1,(205,35))
		else:
			screen.blit(fin,(0,0))
			screen.blit(p2,(205,35))
		if box != pos:
			map = [	['1','2','3'],
					['4','5','6'],
					['7','8','9'],]
			round = True
			pos = 0
		pygame.display.update()

	
	elif pos!=0:
		box = pos
		x, y = pos[0]//170, pos[1]//170
		if round:
			if map[x][y]==str(3*x+y+1):
				map[x][y] = 'X'
				round = not round
		else:
			if  map[x][y]==str(3*x+y+1):
				map[x][y] = 'O'
				round = not round
		redrawGameWindow(map)
	else:
		redrawGameWindow(map)

