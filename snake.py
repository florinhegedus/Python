import pygame
import time
import random

pygame.init()

dis_width=800
dis_height=400
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()

pygame.display.set_caption("Snake by Florin")

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
yellow = (255,255,102)
green = (0,255,0)

clock = pygame.time.Clock()

snake_block=25
snake_speed=15

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 60)

def snake(snake_block, snake_list):
	for x in snake_list:
		pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
	mesg = font_style.render(msg, True, color)
	dis.blit(mesg, [dis_width/3.5, dis_height/1.9])

def score(points):
	value = score_font.render("Your score: " + str(points), True, yellow)
	dis.blit(value, [dis_width/3, dis_height/2.5])

def gameLoop():
	game_over = False
	game_close = False

	x1 = dis_width/2
	y1 = dis_height/2
	x1_change = 0
	y1_change = 0

	snake_list = []
	Length_of_snake = 1

	foodx = round(random.randrange(0, dis_width - snake_block)/25.0)*25.0
	foody = round(random.randrange(0, dis_height - snake_block)/25.0)*25.0

	while not game_over:

		while game_close == True:
			dis.fill(blue)
			message("You lost! Press Q-Quit or C-Play Again", red)
			score(Length_of_snake-1)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					if event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					x1_change = -snake_block
					y1_change = 0
				elif event.key == pygame.K_d:
					x1_change = snake_block
					y1_change = 0
				elif event.key == pygame.K_w:
					x1_change = 0
					y1_change = -snake_block
				elif event.key == pygame.K_s:
					x1_change = 0
					y1_change = snake_block

		if x1>= dis_width or x1 < 0 or y1 >= dis_height or y1<0:
			game_close = True

		x1 += x1_change
		y1 += y1_change
		dis.fill(white)
		pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
		snake_Head = []
		snake_Head.append(x1)
		snake_Head.append(y1)
		snake_list.append(snake_Head)
		if len(snake_list) > Length_of_snake:
			del snake_list[0]

		for x in snake_list[:-1]:
			if x == snake_Head:
				game_close = True

		snake(snake_block, snake_list)

		pygame.display.update()

		if x1 == foodx and y1 == foody:
			foodx = round(random.randrange(0, dis_width - snake_block)/25.0)*25.0
			foody = round(random.randrange(0, dis_height - snake_block)/25.0)*25.0
			Length_of_snake += 1
		clock.tick(snake_speed)

	pygame.quit()
	quit()

gameLoop()