import pygame

pygame.init()

screen = pygame.display.set_mode((1200,800), pygame.RESIZABLE)
blue = (0,0,255)

coords = (0,0)

# piece
# .convert() increases image performance
piece_img = pygame.image.load('images/board.png')
piecex = 350
piecey = 50

blue = (0,0,255)
red = (255, 0, 0)

def piece(x, y):
	# blit means draw
	# drawing image of piece onto window
	screen.blit(piece_img, (x, y))

# Game Loop
running = True
while running:
	# set background color of screen
	screen.fill((255,255,255))

	for event in pygame.event.get():
		# implementing close functionality (close on 'X')
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			coords = pygame.mouse.get_pos()

			if x.collidepoint(coords):
				print(str(coords) + " in circle rect")
			else:
				print(str(coords) + " NOT in circle rect")

			if y.collidepoint(coords):
				print(str(coords) + " in line rect")
			else:
				print(str(coords) + " NOT in line rect")

	piece(piecex, piecey)


	x = pygame.draw.circle(screen, blue, (700, 400), 350, 2)
	z = pygame.draw.circle(screen, blue, (700, 400), 86, 2)

	y = pygame.draw.line(screen, blue, (10, 10), (40, 40), 2)

	

	pygame.display.update()