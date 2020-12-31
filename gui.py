from tkinter import *
import pygame
import math as m

print("Is this thing on?")


class Line():
	def __init__(self, x_1, y_1, slope):
		self.x_1 = x_1
		self.y_1 = y_1
		self.slope = slope

	def y_given_x(self, x):
		return -1*(self.slope*(x - self.x_1) - self.y_1)
	def __str__(self):
		return 'y = ' + str(self.slope) + '(x - ' + str(self.x_1) + ')' + ' + ' + str(self.y_1)

lines = []

for i in range(0, 26, 2):
	lines.append(Line(700, 400, m.tan((i*m.pi)/24)))
	
for l in lines:
	print(l)
	print(l.y_given_x(700))




#root = Tk()

#root.title("3 Man Chess")
# initialize pygame
pygame.init()
# create screen
screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)

# title and icon
pygame.display.set_caption("3 Man chess")


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

def dist(x, y):
	d = m.sqrt((700 - x)**2 + (400 - y)**2)
	return d


def get_position(x, y):
	for i in range(len(lines)):
		#print(lines[i].y_given_x(x))
		try:
			if (y < lines[i].y_given_x(x)) and (y > lines[i + 1].y_given_x(x)):
				print("You are in position " + str(i))
				break
		except:
			pass



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
			
			d = dist(*coords)
			print(coords)
			
			if d > 86:
				if d < 130:
					print("You are in ring 5")
				elif d < 174:
					print("You are in ring 4")
				elif d < 218:
					print("You are in ring 3")
				elif d < 262:
					print("You are in ring 2")
				elif d < 306:
					print("You are in ring 1")
				elif d < 350:
					print("You are in ring 0")
			get_position(*coords)


	piece(piecex, piecey)

	pygame.draw.circle(screen, blue, (700, 400), 350, 2)
	pygame.draw.circle(screen, blue, (700, 400), 306, 2)
	pygame.draw.circle(screen, blue, (700, 400), 262, 2)
	pygame.draw.circle(screen, blue, (700, 400), 218, 2)
	pygame.draw.circle(screen, blue, (700, 400), 174, 2)
	pygame.draw.circle(screen, blue, (700, 400), 130, 2)








	pygame.draw.circle(screen, blue, (700, 400), 86, 2)




	# TWO OPTIONS OF HOW I WILL CREATE REGIONS FOR MY SPOTS IN THE GRID I HAVE DRAWN:

	# 1.) CONSIDER ADDING RECTS INSIDE EACH POLAR REGION AND ROTATING THEM TO BEST APPROXIMATE
	# 2.) do all of the math for the pixel boundaries of the regions

	# line coming from inner ring anlge = 0
	pygame.draw.line(screen, red, (786, 400), (1050, 400), 1)
	# angle = pi
	pygame.draw.line(screen, red, (614, 400), (350, 400), 1)


	# angle = pi/12
	pygame.draw.line(screen, red, (783, 378), (1038, 309), 1)
	# opposite
	pygame.draw.line(screen, red, (617, 422), (362, 491), 1)


	pygame.draw.line(screen, red, (774, 357), (1003, 225), 1)
	pygame.draw.line(screen, red, (626, 443), (397, 575), 1)


	pygame.draw.line(screen, red, (761, 339), (947, 153), 1)
	pygame.draw.line(screen, red, (639, 461), (453, 647), 1)


	pygame.draw.line(screen, red, (743, 326), (875, 97), 1)
	pygame.draw.line(screen, red, (657, 474), (525, 703), 1)


	pygame.draw.line(screen, red, (722, 317), (791, 62), 1)
	pygame.draw.line(screen, red, (678, 483), (609, 738), 1)


	pygame.draw.line(screen, red, (700, 314), (700, 50), 1)
	pygame.draw.line(screen, red, (700, 486), (700, 750), 1)

	pygame.draw.line(screen, red, (678, 317), (609, 62), 1)
	pygame.draw.line(screen, red, (722, 483), (791, 738), 1)

	pygame.draw.line(screen, red, (657, 326), (525, 97), 1)
	pygame.draw.line(screen, red, (743, 474), (875, 703), 1)

	pygame.draw.line(screen, red, (639, 339), (453, 153), 1)
	pygame.draw.line(screen, red, (761, 461), (947, 647), 1)

	pygame.draw.line(screen, red, (626, 357 ), (397, 225), 1)
	pygame.draw.line(screen, red, (774, 443), (1003, 575), 1)

	pygame.draw.line(screen, red, (617, 378), (362, 309), 1)
	pygame.draw.line(screen, red, (783, 422), (1038, 491), 1)

	pygame.draw.line(screen, red, (700, 314), (700, 50), 1)
	pygame.draw.line(screen, red, (700, 486), (700, 750), 1)



	




	# update screen continuously because things will always be changing
	pygame.display.update()