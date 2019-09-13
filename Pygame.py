import pygame
import sys
import random
pygame.init()

WIDTH = 800
HEIGHT = 600
COLOR_R = (255,0,0)
COLOR_B = (0,0,255)
PLAYER_SIZE = 50
PLAYER_POS = [WIDTH/2,HEIGHT-2*PLAYER_SIZE]
BLACK = (0,0,0)
ENEMY_SIZE = 50
ENEMY_POSITION = [random.randint(0,WIDTH-ENEMY_SIZE),0]
enemy_list = [ENEMY_POSITION]
SPEED = 10



screen = pygame.display.set_mode((WIDTH,HEIGHT))
score = 0

game_over = False
clock = pygame.time.Clock()
myFont= pygame.font.SysFont("monospace", 35)
def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) <10 and delay < 0.1:
		x_pos = random.randint(0,WIDTH-ENEMY_SIZE)
		y_pos = 0
		enemy_list.append([x_pos,y_pos])

def set_level(score,SPEED):
	if score < 20:
		SPEED = 3
	elif score < 40:
		SPEED = 4
	elif score < 60:
		SPEED = 5
	else:
		SPEED = 15
	return SPEED	

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen,COLOR_B,(enemy_pos[0],enemy_pos[1],ENEMY_SIZE,ENEMY_SIZE))

def update_enemy_position(enemy_list,score):
	for idx, enemy_pos in enumerate(enemy_list):

		if  enemy_pos[1] >= 0 and  enemy_pos[1] < HEIGHT:
			 enemy_pos[1]= enemy_pos[1]+SPEED
		else:
			enemy_list.pop(idx)
			score = score + 1
	return score

def collission_check(enemy_list, PLAYER_POS):
	for enemy_pos in enemy_list:
		if detect_collission(enemy_pos, PLAYER_POS):
			return True
	return False



def detect_collission(PLAYER_POS, ENEMY_POSITION):
	p_x = PLAYER_POS[0]
	p_y = PLAYER_POS[1]

	e_x = ENEMY_POSITION[0]
	e_y = ENEMY_POSITION[1]

	if (e_x >= p_x and e_x < (p_x + PLAYER_SIZE)) or (p_x >= e_x and p_x < (e_x + ENEMY_SIZE)):
		if (e_y >= p_y and e_y < (p_y + PLAYER_SIZE)) or (p_y >= e_y and p_y < (e_y + ENEMY_SIZE)):
			return True
	return False


while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			x = PLAYER_POS[0]
			y = PLAYER_POS[1]
			if event.key == pygame.K_LEFT:
				x = x- PLAYER_SIZE
			elif event.key == pygame.K_RIGHT:
				x =x+ PLAYER_SIZE
			PLAYER_POS = [x,y]
	screen.fill(BLACK)

	#UPDATING THE POSITION OF THE ENEMY
	

	if detect_collission(PLAYER_POS,ENEMY_POSITION):
		game_over = True
		break		
	drop_enemies(enemy_list)
	score = update_enemy_position(enemy_list,score)
	SPEED = set_level(score, SPEED)
	text = "Score: "+ str(score)
	label = myFont.render(text, 1, (255,255,0))
	screen.blit(label, (WIDTH-200, HEIGHT-40))
	if collission_check(enemy_list,PLAYER_POS):
		game_over = True
		break
	draw_enemies(enemy_list)
	clock.tick(30)
	pygame.draw.rect(screen,COLOR_B,(ENEMY_POSITION[0],ENEMY_POSITION[1],ENEMY_SIZE,ENEMY_SIZE))
	pygame.draw.rect(screen,COLOR_R,(PLAYER_POS[0],PLAYER_POS[1],PLAYER_SIZE,PLAYER_SIZE))
	pygame.display.update()

