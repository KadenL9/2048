import pygame
import random
import time

# initialize pygame module
pygame.init()

# create window
window = pygame.display.set_mode((500, 700));

# colors
white = (255, 255, 255) # white
black  = (0, 0, 0) # black
title_color = (74, 255, 71) # neon greenish
grid_border_color = (167, 5, 247) # purplish
score_border_color = (13, 19, 189) # blueish

color2 = (217, 173, 43) # gold
color4 = (45, 225, 235) # teal
color8 = (252, 50, 43) # maroonish
color16 = (142, 222, 31) # lime greenish
color32 = (232, 30, 151) # pinkish
color64 = (199, 187, 194) # grayish
color128 = (250, 246, 17) # yellow
color256 = (10, 27, 209) # bright blue
color512 = (252, 159, 28) # orange
color1024 = (183, 76, 237) # light purple
color2048 = (76, 237, 119) # weird green
color4096 = (181, 108, 60) # brownish
color8192 = (227, 224, 222) # practically white
color16384 = (255, 107, 228) # light pink
color32768 = (162, 173, 250) # weird blue
color65536 = (171, 237, 104) # yellow-greenish
color131072 = (242, 214, 99) # gold

# fonts
titlefont = pygame.font.SysFont("dejavusans", 45)
scorefont = pygame.font.SysFont("dejavusans", 18)
blockfont = pygame.font.SysFont("dejavusans", 20)

# obtain high score from highscore.txt
highscore_textfile = open("highscore.txt", "r")
highscore = int(highscore_textfile.readline())
highscore_textfile.close()

# player score
score = 0


# function that sets background and layout of game
def set_layout():	
	global score, highscore
	
	# set background to color white
	window.fill(black);

	# draw title
	title = titlefont.render("2048", True, title_color)
	window.blit(title, (100, 75))

	# draw score box
	pygame.draw.rect(window, score_border_color, pygame.Rect(245, 80, 155, 40), 5)
	scoretext = scorefont.render("Score: " + str(score), True, white)
	window.blit(scoretext, (260, 90))
	
	# draw high score box
	pygame.draw.rect(window, score_border_color, pygame.Rect(245, 130, 155, 40), 5)
	highscoretext = scorefont.render("Best: " + str(highscore), True, white)
	window.blit(highscoretext, (260, 140))
	
	# draw grid
	pygame.draw.rect(window, white, pygame.Rect(100, 200, 297, 297), 5)
	for x in range(3):
		pygame.draw.line(window, white, (175 + 73 * x, 200), (175 + 73 * x, 495), 5)
	for x in range(3):
		pygame.draw.line(window, white, (100, 275 + 73 * x), (395, 275 + 73 * x), 5)

	pygame.display.update()
	return

	
# create array to represent grid
grid = []
for a in range(4):
	l = list()
	for b in range(4):
		l.append(0)
	grid.append(l)


# variable that checks if game is over
gameover = False


# function that checks if grid is filled
def grid_filled():
	global grid
	
	for row in range(4):
		for column in range(4):
			if grid[row][column] == 0:
				return False

	return True

	
# function that spawns block
def select_block():
	global grid, gameover, score

	if grid_filled():
		gameover = True

	while True:
		# generate random x and y coordinate on grid from 0-3
		x = random.randint(0, 3)
		y = random.randint(0, 3)

		if grid[x][y] == 0:
			# 10% chance for a 4, 90% chance for a 2
			random_block = random.randint(0, 9)
			if random_block == 0:
				number = 4
			else:
				number = 2
			grid[x][y] = number
			return
	

# function that displays all blocks
def display_blocks():
	# function that displays individual blocks
	def display_block(color, row, column):
		pygame.draw.rect(window, color, pygame.Rect(105 + 73 * row, 205 + 73 * column, 68, 68))
		return

		
	# function to display number on block
	def display_number(number, row, column):
		blocktext = blockfont.render(number, True, black)
		width = (73 - blocktext.get_width()) / 2 - 2
		height = (73 - blocktext.get_height()) / 2 - 1
		window.blit(blocktext, (105 + (73 * row) + width, 205 + (73 * column) + height))
		return

	
	global grid
	for row in range(4):
		for column in range(4):
			if grid[row][column] == 2:
				display_block(color2, row, column)
				display_number("2", row, column)
			elif grid[row][column] == 4:
				display_block(color4, row, column)
				display_number("4", row, column)
			elif grid[row][column] == 8:
				display_block(color8, row, column)
				display_number("8", row, column)
			elif grid[row][column] == 16:
				display_block(color16, row, column)
				display_number("16", row, column)
			elif grid[row][column] == 32:
				display_block(color32, row, column)
				display_number("32", row, column)
			elif grid[row][column] == 64:
				display_block(color64, row, column)
				display_number("64", row, column)
			elif grid[row][column] == 128:
				display_block(color128, row, column)
				display_number("128", row, column)
			elif grid[row][column] == 256:
				display_block(color256, row, column)
				display_number("256", row, column)
			elif grid[row][column] == 512:
				display_block(color512, row, column)
				display_number("512", row, column)
			elif grid[row][column] == 1024:
				display_block(color1024, row, column)
				display_number("1024", row, column)
			elif grid[row][column] == 2048:
				display_block(color2048, row, column)
				display_number("2048", row, column)
			elif grid[row][column] == 4096:
				display_block(color4096, row, column)
				display_number("4096", row, column)
			elif grid[row][column] == 8192:
				display_block(color8192, row, column)
				display_number("8192", row, column)
			elif grid[row][column] == 16384:
				display_block(color16384, row, column)
				display_number("16384", row, column)
			elif grid[row][column] == 32768:
				display_block(color32768, row, column)
				display_number("32768", row, column)
			elif grid[row][column] == 65536:
				display_block(color65536, row, column)
				display_number("65536", row, column)
			elif grid[row][column] == 131072:
				display_block(color131072, row, column)
				display_number("131072", row, column)
				
	pygame.display.update()
	return


# function that moves blocks around
def move_blocks(keys):
	global grid, score

	# check if has actual movement, so doesn't spawn another block when there is no movement
	if keys[pygame.K_DOWN]:
		pass
	elif keys[pygame.K_UP]:
		pass
	elif keys[pygame.K_RIGHT]:
		pass
	elif keys[pygame.K_LEFT]:
		pass
	else:
		return False
		
	if keys[pygame.K_DOWN]:
		for r in range(4):
			for x in range(2, -1, -1):
				# check if block exists in slot
				if grid[r][x] == 0:
					continue

				for y in range(x, 4):
					# check if bottom block is empty
					if grid[r][y] == 0:
						# shift block
						grid[r][y] = grid[r][y - 1]
						grid[r][y - 1] = 0

			# check for combining blocks
			for a in range(2, -1, -1):
				if grid[r][a] == grid[r][a + 1]:
					grid[r][a + 1] *= 2
					grid[r][a] = 0
					score += grid[r][a + 1]

				# shift all blocks down
				for b in range(a, 0, -1):
					if grid[r][b] == 0:
						grid[r][b] = grid[r][b - 1]
						grid[r][b - 1] = 0
						
	elif keys[pygame.K_UP]:
		for r in range(4):
			for x in range(1, 4):
				# check if block exists in slot
				if grid[r][x] == 0:
					continue

				for y in range(x, -1, -1):
					# check if top block is empty
					if grid[r][y] == 0:
						# shift block
						grid[r][y] = grid[r][y + 1]
						grid[r][y + 1] = 0
						
			# check for combining blocks
			for a in range(0, 3):
				if grid[r][a] == grid[r][a + 1]:
					grid[r][a] *= 2
					grid[r][a + 1] = 0
					score += grid[r][a]

				# shift all blocks up
				for b in range(1, a):
					if grid[r][b] == 0:
						grid[r][b] = grid[r][b + 1]
						grid[r][b + 1] = 0
		
	elif keys[pygame.K_RIGHT]:
		for c in range(4):
			for x in range(2, -1, -1):
				# check if block exists in slot
				if grid[x][c] == 0:
					continue

				for y in range(x, 4):
					# check if bottom block is empty
					if grid[y][c] == 0:
						# shift block
						grid[y][c] = grid[y - 1][c]
						grid[y - 1][c] = 0
			
			# check for combining blocks
			for i in range(3, 0, -1):
				if grid[i][c] == grid[i - 1][c]:
					grid[i][c] *= 2
					grid[i - 1][c] = 0
					score += grid[i][c]
				
				# shift all blocks right
				for j in range(i - 1, 0, -1):
					if grid[j][c] == 0:
						grid[j][c] = grid[j - 1][c]
						grid[j - 1][c] = 0
						
	elif keys[pygame.K_LEFT]:
		for c in range(4):
			for x in range(1, 4):
				# check if block exists in slot
				if grid[x][c] == 0:
					continue

				for y in range(x, -1, -1):
					# check if top block is empty
					if grid[y][c] == 0:
						# shift block
						grid[y][c] = grid[y + 1][c]
						grid[y + 1][c] = 0

			# check for combining blocks
			for i in range(0, 3):
				if grid[i][c] == grid[i + 1][c]:
					grid[i][c] *= 2
					grid[i + 1][c] = 0
					score += grid[i][c]

				# shift all blocks right
				for j in range(1, i + 1):
					if grid[j][c] == 0:
						grid[j][c] = grid[j + 1][c]
						grid[j + 1][c] = 0
	else:
		return False

	# update window
	set_layout()
	display_blocks()

	# spawn blocks
	time.sleep(0.25)
	select_block()
	display_blocks()

	return True


# initialize game
set_layout()
select_block()
select_block()
display_blocks()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			keys = pygame.key.get_pressed()
				
			# check for movement
			moved = move_blocks(keys)

			# check to see if game is over
			if gameover:
				if score > highscore:
					# set new high score
					highscore_textfile = open("highscore.txt", "w")
					highscore_textfile.close()
					highscore_textfile = open("highscore.txt", "w")
					highscore_textfile.write(str(score))
					highscore_textfile.close()
				print("gameover!")
