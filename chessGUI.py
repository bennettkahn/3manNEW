from tkinter import *
import pygame
import math as m
import os
import chessbrain as cb
import playersAndGames as p


class Line():
	def __init__(self, x_1, y_1, slope):
		self.x_1 = x_1
		self.y_1 = y_1
		self.slope = slope

	def y_given_x(self, x):
		return -1*(self.slope*(x - self.x_1) - self.y_1)
	def __str__(self):
		return 'y = ' + str(self.slope) + '(x - ' + str(self.x_1) + ')' + ' + ' + str(self.y_1)

class Gui:
	def __init__(self):
		# our vector which allows us to rotate images about topleft point
		self.offset = pygame.math.Vector2(19, -19)
		# store radii of board's rings
		self.rings = {0: 350, 1: 306, 2: 262, 3: 218, 4: 174, 5: 130}
		# store all of the lines on the board
		self.lines = []
		# generate all lines, store them to array
		for i in range(0, 26, 2):
			self.lines.append(Line(700, 400, m.tan((i*m.pi)/24)))

		# initialize pygame
		pygame.init()
		# create screen
		self.screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)

		# title and icon
		pygame.display.set_caption("3 Man chess")
		# on initialization, we always need to load images
		self.load_images()

	def load_images(self):
		# our main board image
		self.board_img = pygame.image.load('images/board.png')

		# LOAD ALL PIECE IMAGES BELOW!
		self.white_king = pygame.image.load('images/whiteKing.png')
		self.white_queen = pygame.image.load('images/whiteQueen.png')
		self.white_rook = pygame.image.load('images/whiteRook.png')
		self.white_knight = pygame.image.load('images/whiteKnight.png')
		self.white_bishop = pygame.image.load('images/whiteBishop.png')
		self.white_pawn = pygame.image.load('images/whitePawn.png')


		self.gray_king = pygame.image.load('images/grayKing.png')
		self.gray_queen = pygame.image.load('images/grayQueen.png')
		self.gray_rook = pygame.image.load('images/grayRook.png')
		self.gray_knight = pygame.image.load('images/grayKnight.png')
		self.gray_bishop = pygame.image.load('images/grayBishop.png')
		self.gray_pawn = pygame.image.load('images/grayPawn.png')


		self.black_king = pygame.image.load('images/blackKing.png')
		self.black_queen = pygame.image.load('images/blackQueen.png')
		self.black_rook = pygame.image.load('images/blackRook.png')
		self.black_knight = pygame.image.load('images/blackKnight.png')
		self.black_bishop = pygame.image.load('images/blackBishop.png')
		self.black_pawn = pygame.image.load('images/blackPawn.png')

	def calc_piece_coords(self, ring, pos):
		''' Given a piece's position and ring, calculate its GUI coordinates '''
		# m.pi/48 is the offset so that the topleft point of the piece is not exactly on the line
		# only works for 5th wring though

		addl_rot = {5: -48, 4: 96.0, 3: 84.0, 2: 72.0, 1: 60.0, 0: 48}
		angle = ((pos - 2) % 24) * (m.pi/12) + (m.pi/addl_rot[ring])

		#print(str(angle))
		radius = self.rings[ring] - 42
		#print(radius)
		# change when i shift board clockwise by two positions!!!!
		if (pos >= 0 and pos <= 7) or (pos >= 20 and pos <= 23):
			x = 700 + abs(radius * m.cos(angle))
		else: 
			x = 700 - abs(radius * m.cos(angle))

		if (pos >= 2 and pos <= 13):
			y = 400 - abs(radius * m.sin(angle))
		else: 
			y = 400 + abs(radius * m.sin(angle))
		#print("%d, %d"% (x, y))
		return (x, y)


	def blitRotate(self, surf, image, pos, originPos, angle):

		# calcaulate the axis aligned bounding box of the rotated image
		w, h       = image.get_size()
		box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
		box_rotate = [p.rotate(angle) for p in box]
		min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
		max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

		# calculate the translation of the pivot 
		pivot        = pygame.math.Vector2(originPos[0], - originPos[1])
		pivot_rotate = pivot.rotate(angle)
		pivot_move   = pivot_rotate - pivot

		# calculate the upper left origin of the rotated image
		origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

		# get a rotated image
		rotated_image = pygame.transform.rotate(image, angle)

		# rotate and blit the image
		surf.blit(rotated_image, origin)

		# draw rectangle around the image
		#pygame.draw.rect (surf, (255, 0, 0), (*origin, *rotated_image.get_size()),2)

	def draw(self, board: cb.Board):
		self.screen.fill((255,255,255))
		# we are always positioning our board at (350, 50)
		self.screen.blit(self.board_img, (350, 50))
		
		# we have to add a little bit to the rotation of the piece placements, depending on which ring they're in
		#addl_rot = {0: 7.5, 1: 6.5, 2: 5.5, 3: 4.5, 4: 3.5, 5: -5}

		# iterate through all spots in the board object's list named board (which is an instance attribrute)
		for i in range(6):
			for j in range(24):
				p = board.board[i][j].Piece
				if p != None and p.killed == False:
					ring = board.board[i][j].ring
					pos = board.board[i][j].pos
					

					if p.color == 'w':
						if p.piece_tag == 'k':
							img = self.white_king
						elif p.piece_tag == 'q':
							img = self.white_queen
						elif p.piece_tag == 'r':
							img = self.white_rook
						elif p.piece_tag == 'kn':
							img = self.white_knight
						elif p.piece_tag == 'b':
							img = self.white_bishop
						elif p.piece_tag[0] == 'p':
							img = self.white_pawn

					elif p.color == 'g':
						if p.piece_tag == 'k':
							img = self.gray_king
						elif p.piece_tag == 'q':
							img = self.gray_queen
						elif p.piece_tag == 'r':
							img = self.gray_rook
						elif p.piece_tag == 'kn':
							img = self.gray_knight
						elif p.piece_tag == 'b':
							img = self.gray_bishop
						elif p.piece_tag[0] == 'p':
							img = self.gray_pawn
					else:
						if p.piece_tag == 'k':
							img = self.black_king
						elif p.piece_tag == 'q':
							img = self.black_queen
						elif p.piece_tag == 'r':
							img = self.black_rook
						elif p.piece_tag == 'kn':
							img = self.black_knight
						elif p.piece_tag == 'b':
							img = self.black_bishop
						elif p.piece_tag[0] == 'p':
							img = self.black_pawn
					rot_angle = 90 + ((pos - 2) % 24)*15 + 7.5
					self.blitRotate(self.screen, img, self.calc_piece_coords(ring, pos), (0,0), rot_angle)
		# we are now doing our screen updating in the draw function
		pygame.display.flip()

		
		#rot_angle = 90 + ((1 - 2) % 24)*15
		#self.blitRotate(self.screen, self.black_queen, self.calc_piece_coords(1, 0), (0,0), rot_angle)

	def calc_ring(self, x, y):
		# calculate distance between mouse click and center of board
		d = m.sqrt((700 - x)**2 + (400 - y)**2)
		ring = None
		if d > 86:
			if d < 130:
				print("You are in ring 5")
				ring = 5
			elif d < 174:
				print("You are in ring 4")
				ring = 4
			elif d < 218:
				print("You are in ring 3")
				ring = 3
			elif d < 262:
				print("You are in ring 2")
				ring = 2
			elif d < 306:
				print("You are in ring 1")
				ring = 1
			elif d < 350:
				print("You are in ring 0")
				ring = 0
		return ring

	def calc_pos(self, x, y):
		# starting with the line towards 0 radians, we rotate counter clockwise
		# if y-coord of mouse click is less than a line but greater than the next (or vice versa), 
		# we have found our position

		for i in range(len(self.lines)):
			if (x > 700):
				if (y < self.lines[i].y_given_x(x)) and (y > self.lines[i + 1].y_given_x(x)):
					p = i
					if (y > 400):
						p += 12
					pos = (p + 2) % 24
					print("You are in position " + str(pos))
					return pos
					break

			else:
				if (y > self.lines[i].y_given_x(x)) and (y < self.lines[i + 1].y_given_x(x)):
					p = i
					if (y > 400):
						p += 12
					pos = (p + 2) % 24
					print("You are in position " + str(pos))
					return pos
					break
	
		if (y < 400):
			print("You are in position 8")
			pos = 8
			return pos
		else:
			print("You are in position 20")
			pos = 20
			return pos
		return None

	def player_move(self, board: cb.Board, player: p.Player, start_ring: int, start_pos: int, end_ring: int, end_pos: int):
		print("in player move")
		# get Spot the Player is starting at
		start_spot = board.get_space(start_ring, start_pos)
		# get Spot the Player is ending at
		end_spot = board.get_space(end_ring, end_pos)
		# create Move object for Player's turn, passing in start and end Spots we determined
		move = p.Move(player, start_spot, end_spot)
		return self.attempt_move(board, move, player)

	def attempt_move(self, board: cb.Board, move: p.Move, player: p.Player) -> bool:
		print("in attempt move")
		# Piece being moved
		move_piece = move.start.Piece
		# if the Player attempts to 'move' a Spot with no Piece, return false
		if (move_piece == None):
			print("returning false because move_piece is none")
			return False

		# the Player can only move a Piece of their own
		if (player.color != move_piece.color):
			print("returning false because of color")
			return False

		# check if piece is moving accross a moat that is not bridged
		#if (move.start >= 0 and move.start <= 7) and (move.end >= 7 )
		
		# see if the Player's King is in check before executing their move
		check_before_move = False
		# this will get us the Spot of the current Player's King
		curr_king_spot = board.get_spot_of_piece(player.color, 'k')
		# if the Player's King is in check
		if (curr_king_spot.is_check(board)):
			print("Your King is in Check! Move him!!!!")
			check_before_move = True
		

		# check if the Player's attempted move is not valid
		if (not(move_piece.valid_move(board, move.start, move.end))):
			print("returning false because not a valid move")
			return False
		if (not(board.is_clear_path(move.start, move.end))):
			print("returning false because there is no clear path to the desired Spot")
			return False

		# simulate moving king to his spot
		board.board[move.end.ring][move.end.pos].Piece = move_piece
		board.board[move.start.ring][move.start.pos].Piece = None

		
		# after executing the move, we test if the Player's King is in check
		check_after_move = False
		# this will get us the Spot of the current Player's King
		curr_king_spot = board.get_spot_of_piece(player.color, 'k')
		# if the Player's King is in check
		if (curr_king_spot.is_check(board)):
			check_after_move = True

		# if the Player was in check before their move AND after their move, they cannot make that move
		# this is assuming that Player is not in checkmate and has a valid move that will get them out of checkmate
		if (check_before_move) and (check_after_move):
			# move piece back
			board.board[move.end.ring][move.end.pos].Piece = None
			board.board[move.start.ring][move.start.pos].Piece = move_piece
			print("returning false because you did not move yourself out of check")
			return False
		if ((not(check_before_move) and (check_after_move))):
			board.board[move.end.ring][move.end.pos].Piece = None
			board.board[move.start.ring][move.start.pos].Piece = move_piece
			print("returning false because you just moved yourself into check")
			return False
	

		board.board[move.end.ring][move.end.pos].Piece = None
		board.board[move.start.ring][move.start.pos].Piece = move_piece
		# Piece at move_piece's ending Spot (assuming move is valid)
		end_piece = move.end.Piece
		#print(end_piece.piece_tag)
		if (end_piece != None):
			end_piece.set_killed()
			# redundant?
			move.piece_killed = end_piece

		return True


	def get_user_input(self, board: cb.Board, curr_player: p.Player):
		from_spot_chosen = False
		to_spot_chosen = False
		running = True
		while not from_spot_chosen or not to_spot_chosen:
			spot_clicked = [None, None]
			
			# set this event to be blocked. speeds it up?
			pygame.event.set_blocked(pygame.MOUSEMOTION)
			event = pygame.event.wait()
			# implementing close functionality (close on 'X')
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				coords = pygame.mouse.get_pos()
				pos = self.calc_pos(*coords)
				ring = self.calc_ring(*coords)
				# list to store spot clicked; first element is position, second is ring
				spot_clicked[0] = ring
				spot_clicked[1] = pos

			if not from_spot_chosen and not to_spot_chosen:
				self.draw(board)
				if spot_clicked[0] != None and spot_clicked[1] != None:
					# store the clicked from spot
					from_spot_list = spot_clicked

					spot_from = board.get_space(from_spot_list[0], from_spot_list[1])

					clicked_from_piece = board.get_space(from_spot_list[0], from_spot_list[1]).Piece
					if clicked_from_piece != None:
						# the user has now clicked the spot he wants to move from
						from_spot_chosen = True

			elif from_spot_chosen and not to_spot_chosen:
				print("In elif branch in get_user_input")
				self.draw(board)
				if spot_clicked[0] != None and spot_clicked[1] != None:
					# store the clicked destination spot
					to_spot_list = spot_clicked

					spot_to = board.get_space(to_spot_list[0], to_spot_list[1])

					clicked_to_piece = board.get_space(to_spot_list[0], to_spot_list[1]).Piece
					if self.player_move(board, curr_player, from_spot_list[0], from_spot_list[1], to_spot_list[0], to_spot_list[1]):
						to_spot_chosen = True
						board.get_space(to_spot_list[0], to_spot_list[1]).Piece = clicked_from_piece
						board.get_space(from_spot_list[0], from_spot_list[1]).Piece = None
					else:
						from_spot_chosen = False

			# update screen continuously because things will always be changing
			#pygame.display.update()

		return (spot_from, spot_to)




			




if __name__ == "__main__":
	B = Gui()
	board = cb.Board()
	B.get_user_input(board)








